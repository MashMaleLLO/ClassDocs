using Calculator465.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using System.Text;
using System.Data;

namespace Calculator465.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [Produces("text/html")]
        public IActionResult Calculate(string number)
        {
            CalculatorModel cal = new CalculatorModel();
            string value = new DataTable().Compute(number, null).ToString();
            cal.CalculateValue = value;
            return Content(cal.CalculateValue, "text/html", Encoding.UTF8);
        }
    }
}
