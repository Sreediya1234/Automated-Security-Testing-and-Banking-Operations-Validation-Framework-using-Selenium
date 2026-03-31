# Automated Security Testing and Banking Operation Validation Framework using Selenium 

## Project Overview

This project implements an automated testing framework for security vulnerabilities and banking operations on a demo banking application (Guru99 Bank). The framework uses Selenium WebDriver and Python to simulate real-life user interactions, test security vulnerabilities, validate banking operations, and automatically generate professional PDF reports with screenshots.

## Key Features

### Security Testing
- SQL injection detection and validation
- Brute Force protection mechanism testing
- Authentication mechanism Validation

### Banking Operations
- Customer registration and management.
- Multiple savings account creation.
- Fund transfer between the accounts.
- Session management and log out validation.

### Documentation and Reporting
- Automatic timestamped screenshots.
- Professional PDF Report generation.
- Color-coded pass/fail status.

## Objectives

- To automate security vulnerability detection by performing SQL injection testing, brute force attack simulationand authentication mechanishm validation.
- To automate core banking operations including customer registration, account creation and secure fund transfers.
- To generate automated test documentation and reporting step wise screenshots and producing timestamp based professiona PDF reports.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Programming Language** | Python |
| **Automation Tool** | Selenium WebDriver |
| **Browser** | Microsoft Edge |
| **Browser Driver** | Edge WebDriver |
| **PDF Generation** | ReportLab |
| **IDE** | VS Code |
| **Package Manager** | pip |
| **OS** | Windows 11 |

## System Architecture
┌─────────────────────────────────────────┐
│      Test Execution Layer (main.py)      │
│   - Orchestrates test sequence           │
│   - Manages browser session              │
│   - Handles errors                       │
└─────────────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────┐
│      Business Logic Layer                │
│   - Login Module                         │
│   - Banking Operations Module            │
│   - Security Tests Module                │
└─────────────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────┐
│      Utility Layer (report_generator.py) │
│   - Screenshot aggregation               │
│   - PDF report generation                │
│   - Result statistics                    │
└─────────────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────┐
│      Selenium WebDriver Layer            │
│   - Element location (ID, XPath, CSS)    │
│   - Wait strategies                      │
│   - Browser event handling               │
└─────────────────────────────────────────┘
                    ▼
┌─────────────────────────────────────────┐
│      Browser Layer (Microsoft Edge)      │
│   - Renders application UI               │
│   - Executes client-side scripts         │
│                                          │
└─────────────────────────────────────────┘

## Test Execution Flow

1. Initialization: WebDriver setup, directory creation.
2. Security Testing: SQL injection, Brute force validation.
3. Banking Operations: Login -> Create Customer -> Create Account -> Second Account -> Fund Transfer -> Log out
4. Report Generation: Screenshot aggregation, PDF creation.

## Results

- Developed an Automated testing framework for banking applications using Selenium Webdriver with Python.
- Achieved Success rate across 8 test cases including security validation and complete banking workflow.
- Generated real customer ID and live bank accounts proving effectiveness.
- Automated documentation and PDF reports saved to customer folders.



