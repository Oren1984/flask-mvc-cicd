# 🧪 QA Documentation – Flask MVC CI/CD Project

This folder contains QA documentation and verification results  
based on Jenkins pipeline logs, Docker build outputs, and Trivy scan reports.

| Document | Description |
|-----------|--------------|
| **01_STP_Test_Plan.xlsx** | Overall test plan for the Flask MVC CI/CD pipeline |
| **02_STD_Test_Cases.xlsx** | Test cases for build, scan, push, and deployment |
| **03_STR_Test_Report.xlsx** | Execution summary including Helm deployment |
| **04_Bug_Report.xlsx** | Recorded Trivy scan timeout issue |

✅ *All stages (Build → Push → Deploy) completed successfully.*  
⚠️ *Trivy scan failed due to timeout; requires re-scan or increased API quota.*
