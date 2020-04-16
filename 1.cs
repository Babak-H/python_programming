using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.IE;
using OpenQA.Selenium.Support.UI;
using Microsoft.Office.Interop.Excel;
using Excel = Microsoft.Office.Interop.Excel;
using System.Threading; // renaming it here for ease of use in the code

namespace CssPGAutomation
{
    class Program
    {
        static void Main(string[] args)
        {
            // PG login
            IWebDriver driver1 = new ChromeDriver();

            // there is an error when you try to maximize window in firefox :
            try
            {
                driver1.Manage().Window.Maximize();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
            driver1.Url = "https://plmprod-3dp.pg.com/3DPassport/login?service=https%3A%2F%2Fplmprod.pg.com%2Fenovia%2Fcommon%2FemxNavigator.jsp";
            driver1.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);


            // enter username and password to login page:
            driver1.FindElement(By.Name("username")).SendKeys("habibnejad.b");
            driver1.FindElement(By.Name("password")).SendKeys("*****" + Keys.Enter);

            // wait for page to load then click on Ok button
            driver1.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver1.FindElement(By.Id("submitButton")).SendKeys(Keys.Enter);

            // CSS login
            IWebDriver driver2 = new InternetExplorerDriver();
            driver2.Url = "http://css.internal.pg.com/";

            // enter credentials for css web page:
            driver2.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);
            driver2.FindElement(By.Id("p_loginid")).SendKeys("cp9974");
            driver2.FindElement(By.Id("p_loginpass")).SendKeys("MoeMoe33" + Keys.Enter);

            ////string mpms = xlRange.Cells[i, 8].Value2.ToString();
            /*
            // Looping through the excel file
            Excel.Application xlApp = new Excel.Application();
            Excel.Workbook xlWorkbook = xlApp.Workbooks.Open(@"C:\Users\u326305\Desktop\New folder\A11.xlsx");
            Excel._Worksheet xlWorksheet = xlWorkbook.Sheets["Sheet22"];
            Excel.Range xlRange = xlWorksheet.UsedRange;
            int rowCount = xlRange.Rows.Count;
            int colCount = xlRange.Columns.Count;
            //TODO create a method to specify the rang of rows
            for (int i = 32; i <= 64; i++)
            {
                for (int j = 1; j <= colCount; j++)
                {
                    Console.WriteLine(i + " " + j + " " + xlRange.Cells[i, j].Value2);
                }
            }
                   string mpms = xlRange.Cells[i, 8].Value2.ToString();
               */

            string mpmp = "MPMP-00027043";    // MPMP-00027043 created
            string mpms = "95843792";

            // enter the mpmp number to P&G searchbar
            Thread.Sleep(25000);
            driver1.FindElement(By.Id("GlobalNewTEXT")).SendKeys(mpmp + Keys.Enter);

            // wait then try to find a result with 'Preliminary' text and then find and click on it:
            Thread.Sleep(5000);
            driver1.SwitchTo().Frame("windowShadeFrame");
            driver1.SwitchTo().Frame("structure_browser");

            // Checking if the MPMP is Preliminary :
            if (driver1.FindElement(By.XPath("//*[@id='bodyTable']/tbody/tr[2]")).FindElement(By.XPath("//td[contains(@title,'Preliminary')]")).Displayed)
            {
                Console.WriteLine(driver1.FindElement(By.XPath("//*[@id='bodyTable']/tbody/tr[2]/td[4]")).Text);
                driver1.FindElement(By.XPath("//td[contains(@title,'MPMP-00027043')]")).FindElement(By.XPath("//a[contains(@data-icon,'images/packagingmaterial.gif')]")).Click();
                try
                {
                    driver1.FindElement(By.XPath("//td[contains(@title,'MPMP-00027043')]")).FindElement(By.XPath("//a[contains(@data-icon,'images/packagingmaterial.gif')]")).Click();
                }
                catch (Exception e) { }

                // search for mpms in CSS website :
                driver2.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);
                driver2.FindElement(By.Name("GCASCode")).SendKeys(mpms + Keys.Enter);
                driver2.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);

                // click on the result :
                driver2.FindElement(By.Id("DisplayArea")).FindElement(By.XPath("//a[contains(@href,'http://css.internal.pg.com/ViewTab.action?id=')]")).Click();
                driver2.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(5);

                // you need to refresh the page :
                driver2.Navigate().Refresh();

                // get the ATS from css page :
                String hasATS_css = driver2.FindElement(By.XPath("//*[@name='top']/p/table[2]/tbody/tr[2]/td[7]/table/tbody/tr[2]/td[2]")).Text;

                if (String.IsNullOrEmpty(hasATS_css))
                {
                    // write in some kind text file that this CSS file is empty!!
                }

                Thread.Sleep(3000);
                driver1.SwitchTo().DefaultContent();
                driver1.SwitchTo().Frame("content");
                driver1.SwitchTo().Frame("detailsDisplay");
                driver1.SwitchTo().Frame("portalDisplay");
                driver1.SwitchTo().Frame("pgVPDSectionAttributes");


                // getting elements from pg page before going to edit mode:
                string hasATS_pg = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[2]/td[4]")).Text;
                if (!hasATS_css.Equals(hasATS_pg))
                {
                    //there is no option in edit mode to change ats!!!!!
                }
                string pg_manufacturing = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[11]/td[4]")).Text;
                string pg_brand = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[13]/td[2]")).Text;
                string pg_unitMeasure = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[16]/td[2]")).Text;
                string pg_localDescription = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[17]/td[2]")).Text;
                string pg_packagingSizeUnit = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[21]/td[2]")).Text;
                string pg_comment = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[29]/td[2]")).Text;
                string pg_primaryOrg = driver1.FindElement(By.XPath("//*[@name = 'frmFormView']/table/tbody/tr[33]/td[2]")).Text;

                Thread.Sleep(6000);
                // click pencil button to go to edit mode :
                driver1.FindElement(By.XPath("//*[@id='pgVPDSectionAttributeEditAll']/img")).Click();

                // accept the alert pop up about comment:
                driver1.SwitchTo().Alert().Accept();

                // set title and description
                Thread.Sleep(2000);
                driver1.FindElement(By.Id("Title")).Clear();
                driver1.FindElement(By.Id("Title")).SendKeys("xxxxxxx");
                driver1.FindElement(By.XPath("//textarea[@id='Description']")).Clear();
                driver1.FindElement(By.XPath("//textarea[@id='Description']")).SendKeys("xxxxxxxxx");

                //change segment from drop-down menu
                SelectElement selectSegment = new SelectElement(driver1.FindElement(By.Id("SegmentId")));
                selectSegment.SelectByText("All Other Air Care");

                //changing the owner:
                //string currentHandle = driver1.CurrentWindowHandle;
                //PopupWindowFinder finder = new PopupWindowFinder(driver1);
                //string popupWindowHandle = finder.Click(driver1.FindElement(By.XPath("//*[@id='calc_Stage']/td[4]/table/tbody/tr/td[2]/input")));
                //Thread.Sleep(2000);
                //driver1.FindElement(By.XPath("//body/div[2]/form/table/tbody/tr[9]/td[4]/table/tbody/tr/td[2]/input")).Click();

                //driver1.SwitchTo().Window(popupWindowHandle);

                //// there is an error when you try to maximize window in firefox :
                //try
                //{
                //    driver1.Manage().Window.Maximize();
                //}
                //catch (Exception e)
                //{
                //    Console.WriteLine(e);
                //}

                //driver1.FindElement(By.XPath("//*[@id='searchBody']/ul/li[2]/span/input")).SendKeys("Lonneman.mt");
                ////
                //driver1.FindElement(By.Id("mx_btn-search")).Click();
                //Thread.Sleep(5000);
                //driver1.FindElement(By.Id("rmbrow-0,0")).Click();
                //driver1.FindElement(By.XPath("//*[@id='divPageFootButtons']/table/tbody/tr/td[2]/a/button")).Submit();


                // Setting manufacturing status in edit mode if it is different from css_lifeCycle :
                string css_lifeCycle = driver2.FindElement(By.XPath("//body/table/tbody/tr[6]/td[2]")).Text;
                if (!pg_manufacturing.ToLower().Equals(css_lifeCycle.ToLower()))
                {
                    SelectElement selectManuStat = new SelectElement(driver1.FindElement(By.Id("StatusId")));
                    selectManuStat.SelectByText("PLANNING");
                }
                if (!pg_manufacturing.ToLower().Equals("production"))
                {
                    //write in a txt file that this record has a problem
                }


                // // Reason For Change :
                driver1.FindElement(By.Name("Reason For change")).Clear();
                driver1.FindElement(By.Name("Reason For change")).SendKeys("XXXXXX");

                // Brand :
                if (!String.IsNullOrEmpty(pg_brand))
                {
                    // find it in CSS  
                    SelectElement brandElement = new SelectElement(driver1.FindElement(By.Id("BrandMultiSelectId")));
                    brandElement.SelectByText("AccuClear");
                }

                // Class :
                SelectElement classElement = new SelectElement(driver1.FindElement(By.Id("ClassId")));
                classElement.SelectByText("Aldehydes");

                // Reported Function
                SelectElement reportElement = new SelectElement(driver1.FindElement(By.Name("Reported Function")));
                reportElement.SelectByText("Absorbency Aid");

                // unit of measure :
                if (!pg_unitMeasure.ToLower().Equals("Millimeter’"))
                {
                    SelectElement uomElement = new SelectElement(driver1.FindElement(By.Name("NonMandatory Dimension Unit Of Measure Picklist")));
                    uomElement.SelectByText("Millimeter");
                }

                // local description :
                if (!String.IsNullOrEmpty(pg_localDescription))
                {
                    string css_pg_localDescription = driver2.FindElement(By.XPath("//body/table/tbody/tr[7]/td[2]")).Text;
                    driver1.FindElement(By.Name("Local Description")).Clear();
                    driver1.FindElement(By.Name("Local Description")).SendKeys("1234567");
                }

                // Packaging material :
                string css_packagingMaterialType = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[7]/td[2]")).Text;
                SelectElement packageMaterialElement = new SelectElement(driver1.FindElement(By.Name("Packaging Material Type")));
                packageMaterialElement.SelectByText("Device- Assembly");

                // Packaging component type :
                string css_packagingComponentType = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[10]/td[2]")).Text;
                SelectElement packageComponentElement = new SelectElement(driver1.FindElement(By.Name("Packaging Component Type")));
                packageComponentElement.SelectByText("ACTUATOR");

                // Packaging size : 
                string css_packagingSize = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[8]/td[2]")).Text;
                if (!String.IsNullOrEmpty(css_packagingSize))
                {
                    // Packaging Size
                    driver1.FindElement(By.Name("Packaging Size")).Clear();
                    driver1.FindElement(By.Name("Packaging Size")).SendKeys("123456");
                }


                // Unit of measurement material :
                string css_packagingSizeUnit = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[8]/td[4]")).Text;
                if (!String.IsNullOrEmpty(css_packagingSize))
                {
                    SelectElement UoMMaterialElement = new SelectElement(driver1.FindElement(By.Name("Packaging Size UoM")));

                    if (String.IsNullOrEmpty(pg_packagingSizeUnit))
                    {
                        UoMMaterialElement.SelectByText("Alkaline Protease Units");
                    }
                    else
                    {
                        // get it from excel sheet
                        UoMMaterialElement.SelectByText("");
                    }
                }

                // Printing process :
                SelectElement printingProccessElement = new SelectElement(driver1.FindElement(By.Name("Printing Process")));
                printingProccessElement.SelectByValue("");

                // Shipping information :
                string css_shippingInformation = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[17]/td[2]")).Text;
                string pg__shippingInformation = driver1.FindElement(By.Name("Shipping Information")).Text;
                if (!String.IsNullOrEmpty(pg__shippingInformation))
                {
                    driver1.FindElement(By.Name("Shipping Information")).Clear();
                    driver1.FindElement(By.Name("Shipping Information")).SendKeys("1234567");
                }

                // Labeling information :
                string css_labelingInformation = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[18]/td[2]")).Text;
                string pg__labelingInformation = driver1.FindElement(By.Name("Labeling Information")).Text;
                if (!String.IsNullOrEmpty(pg__labelingInformation))
                {
                    driver1.FindElement(By.Name("Labeling Information")).Clear();
                    driver1.FindElement(By.Name("Labeling Information")).SendKeys("1234567");
                }

                // storage information :
                string css_storageInformation = driver2.FindElement(By.XPath("//body/table[3]/tbody/tr[19]/td[2]")).Text;
                string pg__storageInformation = driver1.FindElement(By.Name("Storage Information")).Text;
                if (!String.IsNullOrEmpty(pg__storageInformation))
                {
                    driver1.FindElement(By.Name("Storage Information")).Clear();
                    driver1.FindElement(By.Name("Storage Information")).SendKeys("1234567");
                }

                // Storage Temperature Limits
                driver1.FindElement(By.Name("Storage Temperature Limits")).Clear();

                // length/height :
                driver1.FindElement(By.Name("Inner Dimension Height")).Clear();
                driver1.FindElement(By.Name("Inner Dimension Height")).SendKeys("0.0");

                driver1.FindElement(By.Name("Inner Dimension Length")).Clear();
                driver1.FindElement(By.Name("Inner Dimension Length")).SendKeys("0.0");

                driver1.FindElement(By.Name("NonMandatory Outer Dimension Width")).Clear();
                driver1.FindElement(By.Name("NonMandatory Outer Dimension Width")).SendKeys("0.0");

                driver1.FindElement(By.Name("NonMandatory Outer Dimension Length")).Clear();
                driver1.FindElement(By.Name("NonMandatory Outer Dimension Length")).SendKeys("0.0");

                driver1.FindElement(By.Name("NonMandatory Outer Dimension Height")).Clear();
                driver1.FindElement(By.Name("NonMandatory Outer Dimension Height")).SendKeys("0.0");



                // Comment :
                if (!String.IsNullOrEmpty(pg_comment))
                {
                    //comment in PG
                    string css_materialOfConstruction = driver2.FindElement(By.XPath("//body/table[2]/tbody/tr/td[1]/label")).Text;
                    List<string> css_desc = new List<string>();
                    if (driver2.FindElement(By.XPath("//body/table[2]/tbody/tr/td[2]/table")).Displayed)
                    {
                        // looping through the table
                        IWebElement table = driver2.FindElement(By.XPath("//body/table[2]/tbody/tr/td[2]/table"));
                        IList<IWebElement> rows = table.FindElements(By.TagName("tr"));
                        int rowSize = rows.Count;
                        Console.WriteLine(rowSize);
                        for (int i = 2; i <= rows.Count; i++)
                        {
                            css_desc.Add(driver2.FindElement(By.XPath("//body/table[2]/tbody/tr/td[2]/table/tbody/tr[" + i + "]/td[4]")).Text);
                        }
                    }
                    string descriptions = string.Join(" ", css_desc.ToArray());
                    string pg_c = css_materialOfConstruction + descriptions;

                    driver1.FindElement(By.Id("Comments")).Clear();
                    driver1.FindElement(By.Id("Comments")).SendKeys(pg_c);
                }

                // 	Obsolete data : is not available to edit
                driver1.FindElement(By.Name("Project MileStone")).Clear();

                // Primary organization :
                driver2.FindElement(By.XPath("//body/a/p/table[3]/tbody/tr/td/img[6]")).Click();
                string css_primaryOrg = driver2.FindElement(By.XPath("//body/table/tbody/tr[3]/td[2]")).Text;
                // problem adding it into PG!!!

                // Secondary organization :
                string css_secondaryOrg = driver2.FindElement(By.XPath("//body/table[2]/tbody/tr[6]/td[2]")).Text;


                // Going to TABLES tab :
                driver1.SwitchTo().DefaultContent();
                driver1.SwitchTo().Frame("content");
                driver1.SwitchTo().Frame("detailsDisplay");
                driver1.SwitchTo().Frame("portalDisplay");
                driver1.FindElement(By.XPath("//body/div/div/div/div/table/tbody/tr/td[2]/table/tbody/tr/td")).Click();

                // Selecting 'Local' from show characteristics :
                driver1.SwitchTo().DefaultContent();
                driver1.SwitchTo().Frame("content");
                driver1.SwitchTo().Frame("detailsDisplay");
                driver1.SwitchTo().Frame("portalDisplay");
                driver1.SwitchTo().Frame("CPNProductDataViewTables");
                SelectElement charSelect = new SelectElement(driver1.FindElement(By.XPath("//body/form/div/div/div/div/table/tbody/tr/td[3]/select")));
                charSelect.SelectByText("Local");
            }
        }
    }
    }
