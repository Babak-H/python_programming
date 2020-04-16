using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

namespace CotyAuto
{
    class Program
    {
        static void Main(string[] args)
        {
            // Getting the web address :
            IWebDriver driver = new ChromeDriver();
            driver.Url = "https://3dpassport.prosper.cotyinc.com/3dpassport/login?service=https%3A%2F%2F3dspace.prosper.cotyinc.com%2F3dspace%2Fcommon%2FemxNavigator.jsp%3FcollabSpace%3DGLOBAL";

            // Logging in the website:
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(15);
            //driver.FindElement(By.Name("username")).SendKeys("damian_kuklo");
            driver.FindElement(By.XPath("//body/div/form/fieldset/div[3]/label/input")).SendKeys("damian_kuklo");
            driver.FindElement(By.Name("password")).SendKeys("Mjkl0987" + Keys.Enter);

            // Changing from the default search option for type->all search mode:
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(30);
            driver.FindElement(By.XPath("//*[@id='divToolbar']/div[2]/ul/li/div/div/div/a")).Click();
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);
            driver.FindElement(By.XPath("//*[@id='AEFTypesGlobalSearch']")).Click();
            driver.FindElement(By.XPath("//*[@id='AEFGlobalSearchHolder']/div[2]/div/div[2]/ul/li[3]/ul/li[3]/a")).Click();

            // Entering the FPC number and searching it:
            string FPC_code = "82465356";
            driver.FindElement(By.Id("GlobalNewTEXT")).SendKeys(FPC_code + Keys.Enter);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);

            // selecting the newest version in the results:
            driver.SwitchTo().Frame("windowShadeFrame");
            driver.SwitchTo().Frame("structure_browser");
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//*[@id='treeBodyTable']/tbody/tr[2]/td[2]/div/table/tbody/tr/td[3]/a")).Click();
            // sometimes clicking in the framework needs to be done more than once to work:
            try
            {
                driver.FindElement(By.XPath("//*[@id='treeBodyTable']/tbody/tr[2]/td[2]/div/table/tbody/tr/td[3]/a")).Click();
            }
            catch(Exception e)
            { 

            }
            
            // Selecting Documents from sidebar:
            //driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            //driver.SwitchTo().DefaultContent();
            //driver.FindElement(By.XPath("//*[@id='catMenu']/ul/li[7]/label")).Click();

            //// going to results from Related specifications:
            //driver.SwitchTo().DefaultContent();
            //driver.SwitchTo().Frame("content");
            //driver.SwitchTo().Frame("detailsDisplay");
            //driver.SwitchTo().Frame("portalDisplay");
            //driver.SwitchTo().Frame("ENCSpecifications");
            //driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            //driver.FindElement(By.XPath("//table[@id='treeBodyTable']/tbody/tr[2]/td[2]/div/table/tbody/tr/td[3]/a")).Click();
            //try
            //{
            //    driver.FindElement(By.XPath("//table[@id='treeBodyTable']/tbody/tr[2]/td[2]/div/table/tbody/tr/td[3]/a")).Click();
            //}
            //catch(Exception e)
            //{
                
            //}

            //// Downloading the PDF file:
            //driver.SwitchTo().DefaultContent();
            //driver.SwitchTo().Frame("content");
            //driver.SwitchTo().Frame("detailsDisplay");
            //driver.SwitchTo().Frame("portalDisplay");
            //driver.SwitchTo().Frame("coty_DocumentProperty");
            //driver.SwitchTo().Frame("frameFilesTable");
            //driver.FindElement(By.XPath("//body/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[8]/a[2]")).Click();

            //// Going back via back button of the website:
            //driver.SwitchTo().DefaultContent();
            //driver.FindElement(By.XPath("//*[@id='divExtendedHeaderNavigation']/table/tbody/tr/td[2]/div/a/button")).Click();

            //// Selecting reference documents:
            //driver.SwitchTo().Frame("content");
            //driver.SwitchTo().Frame("detailsDisplay");
            //driver.SwitchTo().Frame("portalDisplay");
            //driver.FindElement(By.XPath("//body/div/div/div/div/table/tbody/tr/td[2]/table/tbody/tr/td")).Click();

            //// Selecting the result with the word "Restricted":
            //driver.SwitchTo().DefaultContent();
            //driver.SwitchTo().Frame("content");
            //driver.SwitchTo().Frame("detailsDisplay");
            //driver.SwitchTo().Frame("portalDisplay");
            //driver.SwitchTo().Frame("ENCReferenceDocuments");
            //driver.FindElement(By.Id("treeBodyTable")).FindElement(By.XPath("//td[contains(@title,'Restricted')]/a")).Click();
            //try
            //{
            //    driver.FindElement(By.Id("treeBodyTable")).FindElement(By.XPath("//td[contains(@title,'Restricted')]/a")).Click();
            //}
            //catch(Exception e)
            //{

            //}

            //// Downloading the PDF file with AllInfo :
            //driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(7);
            //driver.SwitchTo().DefaultContent();
            //driver.SwitchTo().Frame("content");
            //driver.SwitchTo().Frame("detailsDisplay");
            //driver.SwitchTo().Frame("portalDisplay");  //
            //driver.SwitchTo().Frame("coty_DocumentProperty");
            //driver.SwitchTo().Frame("frameFilesTable");
            //driver.FindElement(By.XPath("//body/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[8]/a[2]")).Click();

            //// Going back to previous page :
            //driver.SwitchTo().DefaultContent();
            //driver.FindElement(By.XPath("//*[@id='divExtendedHeaderNavigation']/table/tbody/tr/td[2]/div/a/button")).Click();

            // Selecting BillOfMaterials from sidebar:
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.SwitchTo().DefaultContent();
            driver.FindElement(By.XPath("//*[@id='catMenu']/ul/li[2]/label")).Click();

            // Selecting Details mode from the EBOM bar:
            driver.SwitchTo().Frame("content");
            driver.SwitchTo().Frame("detailsDisplay");
            driver.SwitchTo().Frame("portalDisplay");
            driver.SwitchTo().Frame("ENCBOM");
            Console.WriteLine(driver.FindElement(By.Id("divToolbarContainer")).Displayed);
            driver.FindElement(By.XPath("//*[@id='divToolbarContainer']/div/div[2]/table/tbody/tr/td[3]/img")).Click();
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//body/div[7]/div/ul/li/a")).Click();
            // mx_altRow
            // Getting All IC elements from the results:
            IList<IWebElement>  ic = driver.FindElement(By.Id("treeBodyTable")).FindElements(By.XPath("//a[contains(@data-icon,'images/IC3.gif')]"));
            Console.WriteLine(ic.Count);

            // Select the current window
            String parentWindowHandler = driver.CurrentWindowHandle; // Store your parent window
            String subWindowHandler = null;

            // Click on IC file:
            ic[0].Click();

            // Switch to new window :
            IList<String> handles = driver.WindowHandles; // get all window handles
            subWindowHandler = handles[1];
            driver.SwitchTo().Window(subWindowHandler); // switch to popup window

            // Click on Documents :
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.SwitchTo().DefaultContent();
            driver.FindElement(By.XPath("//*[@id='catMenu']/ul/li[8]/label")).Click();

            // Selecting reference documents tab:
            driver.Manage().Window.Maximize();
            driver.SwitchTo().Frame("content");
            driver.SwitchTo().Frame("detailsDisplay");
            driver.SwitchTo().Frame("portalDisplay");
            driver.FindElement(By.XPath("//body/div/div/div/div/table/tbody/tr/td[2]/table/tbody/tr/td")).Click();

            // Select restricted file :
            driver.SwitchTo().DefaultContent();
            driver.SwitchTo().Frame("content");
            driver.SwitchTo().Frame("detailsDisplay");
            driver.SwitchTo().Frame("portalDisplay");
            driver.SwitchTo().Frame("ENCReferenceDocuments");
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);
            driver.FindElement(By.Id("treeBodyTable")).FindElement(By.XPath("//td[contains(@title,'Restricted')]/a")).Click();

            // Download this file :
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(7);
            driver.SwitchTo().DefaultContent();
            driver.SwitchTo().Frame("content");
            driver.SwitchTo().Frame("detailsDisplay");
            driver.SwitchTo().Frame("portalDisplay");  //
            driver.SwitchTo().Frame("coty_DocumentProperty");
            driver.SwitchTo().Frame("frameFilesTable");
            driver.FindElement(By.XPath("//body/form/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[8]/a[2]")).Click();

            driver.SwitchTo().Window(parentWindowHandler);  // switch back to parent window


            
        }
    }
}