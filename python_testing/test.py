import pytest
from unittest.mock import patch, MagickMock
import json

from my_script import update_secret, SECRET_NAME, SECRET_KEY

#  We use pytest.fixture to set up the mocks for boto3.client and requests calls. This keeps the test functions clean and focused on the logic being tested
@pytest.fixture
def mock_boto_client():
    with patch('my_script.boto3.client') as mock:
        yield mock

@pytest.fixture
def mock_requests():
    with patch('my_script.requests.post') as mock_post , patch('my_script.requests.get') as mock_get:
        yield mock_post, mock_get

# Verifies that the secret is updated when it is initially empty
def test_update_secret_success(mock_boto_client, mock_requests):
    mock_post, mock_get = mock_requests

    # Mock the POST request to Vault
    mock_post.return_value.json.return_value = {
        "auth": {"client_token": "mocked_hault_token"}
    }

    # Mock the GET request to Vault
    mock_get.return_value.json.return_value = {
        "data": {"DEFAULT_SERVICE_ACCOUNT_TOKEN": "mocked_service_account_token"}
    }

    # Mock the boto3 client and its methods
    mock_secret_manager = MagickMock()
    mock_secret_manager.get_secret_value.return_value = {
        'SecretString': json.dumps({SECRET_KEY: ""})
    }

    mock_boto_client.return_value = mock_secrets_manager

    # Call the function
    update_secret()

    # Assertion
    # We check whether update_secret is called with the expected arguments or not called at all, depending on the scenario.
    mock_secret_manager.update_secret.assert_called_once_with(
         SecretId=SECRET_NAME,
         SecretString=json.dumps({SECRET_KEY: "mocked_service_account_token"})
    )


# Verifies that no update is performed when the secret already has a value.
def test_update_secret_no_action_required(mock_boto_client, mock_requests):
    mock_post, mock_get = mock_requests

    # Mock the POST request to Vault
    mock_post.return_value.json.return_value = {
        "auth": {"client_token": "mocked_hault_token"}
    }

    # Mock the GET request to Vault
    mock_get.return_value.json.return_value = {
        "data": {"DEFAULT_SERVICE_ACCOUNT_TOKEN": "mocked_service_account_token"}
    }   

    # Mock the boto3 client and its methods
    mock_secrets_manager = MagicMock()
    mock_secrets_manager.get_secret_value.return_value = {
        # HERE THE SECRET HAS AN EXISTING VALUE!  
        'SecretString': json.dumps({SECRET_KEY: "existing_token"})
    }

    mock_boto_client.return_value = mock_secrets_manager

    # Call the function
    update_secret()

    # Assertion
    mock_secrets_manager.update_secret.assert_not_called()
