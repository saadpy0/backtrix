{
  "projectMvpAnalysis": {
    "mvpDescription": {
      "purpose": "Enable data scientists and quant analysts to quickly test trading strategies by simply describing them in plain English — no coding required.",
      "coreFeatures": [
        {
          "id": 1,
          "name": "Data Input",
          "details": [
            "Upload CSV/Excel files with historical price data",
            "Or fetch historical market data by entering stock ticker and date range"
          ]
        },
        {
          "id": 2,
          "name": "Data Processing",
          "details": [
            "Auto-parse and clean input data",
            "Generate summary statistics and basic visualizations (price charts, volume, moving averages)"
          ]
        },
        {
          "id": 3,
          "name": "Natural Language Strategy Input",
          "details": [
            "Text box for users to describe simple trading strategies in natural language (e.g., moving average crossovers)"
          ]
        },
        {
          "id": 4,
          "name": "AI-Powered Code Generation",
          "details": [
            "Convert natural language strategy descriptions into Python backtest code automatically using AI (e.g., OpenAI API or Cursor AI)"
          ]
        },
        {
          "id": 5,
          "name": "Backtest Execution",
          "details": [
            "Run generated code safely on backend to simulate strategy performance using historical data"
          ]
        },
        {
          "id": 6,
          "name": "Results Visualization",
          "details": [
            "Show equity curve charts and key performance metrics (total return, max drawdown, win rate, Sharpe ratio)"
          ]
        }
      ],
      "techStack": {
        "backend": "FastAPI (Python) for API and backtest execution",
        "frontend": "Next.js + Plotly.js for UI and charts",
        "aiIntegration": "OpenAI API / Cursor AI for code generation",
        "dataHandling": "Pandas, yfinance",
        "databaseAndAuth": "Supabase"
      },
      "valueProposition": "Simplifies the complex and technical task of quantitative strategy backtesting by making it accessible through natural language — ideal for beginners and experienced quants alike."
    },
    "architecture": {
      "title": "AI-Powered Natural Language Quant Strategy Builder - MVP Architecture",
      "overallDiagramConceptual": [
        "+---------------------+      +---------------------+      +---------------------+",
        "|   Client (Next.js)  |----->|  Backend (FastAPI)  |<---->|  Supabase (DB/Auth) |",
        "+---------------------+      +---------------------+      +---------------------+",
        "        ^      |                      |        ^",
        "        |      |                      |        |",
        "        |      +----------------------+        | (yfinance)",
        "        |      (Natural Language,     |        |",
        "        |       Data Upload/Fetch)    v        |",
        "        |                             +---------------------+",
        "        |                             |   AI Service        |",
        "        |                             | (OpenAI/Cursor AI)  |",
        "        +-----------------------------+---------------------+",
        "        (Results, Visualizations)      (Python Code Gen)"
      ],
      "frontend": {
        "name": "Frontend (Next.js + Plotly.js)",
        "description": "Manages user interaction, data input, strategy description, and visualization of results.",
        "fileFolderStructure": {
          "root": "frontend/",
          "children": [
            {"name": "public/", "description": "Static assets (images, favicons)"},
            {
              "name": "src/",
              "children": [
                {
                  "name": "app/",
                  "description": "Next.js 13+ App Router",
                  "children": [
                    {"name": "(auth)/", "description": "Authentication related pages", "children": [{"name": "login/page.tsx"}, {"name": "signup/page.tsx"}]},
                    {"name": "dashboard/", "description": "Main application area", "children": [{"name": "page.tsx"}, {"name": "layout.tsx"}]},
                    {"name": "layout.tsx", "description": "Root layout"},
                    {"name": "page.tsx", "description": "Landing page (optional)"}
                  ]
                },
                {
                  "name": "components/",
                  "description": "Reusable UI components",
                  "children": [
                    {"name": "ui/", "description": "Generic UI elements"},
                    {"name": "auth/", "description": "Auth related components"},
                    {"name": "data-input/", "description": "Components for data input", "children": [{"name": "FileUpload.tsx"}, {"name": "TickerForm.tsx"}]},
                    {"name": "strategy-input/", "description": "Component for NL strategy input (StrategyTextBox.tsx)"},
                    {"name": "visualizations/", "description": "Charting components", "children": [{"name": "PriceChart.tsx"}, {"name": "ResultsDisplay.tsx"}]},
                    {"name": "common/", "description": "Common components"}
                  ]
                },
                {"name": "contexts/", "description": "React Context API for global state"},
                {"name": "hooks/", "description": "Custom React hooks"},
                {"name": "services/", "description": "API call functions (api.ts, supabaseClient.ts)"},
                {"name": "store/", "description": "Optional: Global state management (Zustand, Jotai)"},
                {"name": "lib/", "description": "Utility functions, constants", "children": [{"name": "utils.ts"}, {"name": "supabaseClient.ts"}]},
                {"name": "styles/", "description": "Global styles, Tailwind CSS config"}
              ]
            },
            {"name": "next.config.js"},
            {"name": "tsconfig.json"},
            {"name": "package.json"},
            {"name": "tailwind.config.ts"}
          ]
        },
        "componentResponsibilities": [
          {"component": "src/app/(auth)/", "responsibility": "Handles user login and registration pages. Interacts with Supabase for authentication."},
          {"component": "src/app/dashboard/page.tsx", "responsibility": "Main application page orchestrating data input, strategy input, and results display."},
          {"component": "src/components/data-input/FileUpload.tsx", "responsibility": "Allows users to upload CSV/Excel files. Sends file to backend."},
          {"component": "src/components/data-input/TickerForm.tsx", "responsibility": "Allows users to input stock ticker and date range. Sends request to backend."},
          {"component": "src/components/strategy-input/StrategyTextBox.tsx", "responsibility": "Provides a text area for users to describe their strategy in natural language."},
          {"component": "src/components/visualizations/PriceChart.tsx", "responsibility": "Displays initial price charts, volume, moving averages using Plotly.js."},
          {"component": "src/components/visualizations/ResultsDisplay.tsx", "responsibility": "Shows equity curve, performance metrics from backtest results."},
          {"component": "src/contexts/ or src/store/", "responsibility": "Manages global application state (auth status, data, strategy, results, loading states)."},
          {"component": "src/services/api.ts", "responsibility": "Contains functions for HTTP requests to the FastAPI backend."},
          {"component": "src/lib/supabaseClient.ts", "responsibility": "Initializes and exports the Supabase client."}
        ],
        "stateManagement": {
          "local": "Local Component State (useState, useReducer) for form inputs, UI toggles.",
          "global": "Global State (Context API / Zustand / Jotai) for user auth, data, strategy text, backtest results, loading states. Updated via user interactions and API responses."
        },
        "serviceConnections": [
          "Communicates with Backend (FastAPI) via RESTful API for auth, data operations, strategy submission, and results retrieval.",
          "Communicates with Supabase directly for client-side authentication."
        ]
      },
      "backend": {
        "name": "Backend (FastAPI - Python)",
        "description": "Handles business logic, data processing, AI integration, backtest execution, and serves as the API for the frontend.",
        "fileFolderStructure": {
          "root": "backend/",
          "children": [
            {
              "name": "app/",
              "children": [
                {"name": "__init__.py"},
                {"name": "main.py", "description": "FastAPI app instantiation, middleware, root routers"},
                {
                  "name": "api/", "description": "API Endpoints (Routers)",
                  "children": [
                    {"name": "__init__.py"},
                    {"name": "v1/", "children": [
                      {"name": "__init__.py"},
                      {"name": "endpoints/", "children": [
                        {"name": "__init__.py"},
                        {"name": "auth.py", "description": "Authentication endpoints"},
                        {"name": "data.py", "description": "Data input, processing, summary endpoints"},
                        {"name": "strategy.py", "description": "Strategy submission, code gen, backtest execution"}
                      ]},
                      {"name": "api.py", "description": "Aggregates endpoint routers"}
                    ]}
                  ]
                },
                {"name": "core/", "description": "Core configurations, settings", "children": [{"name": "__init__.py"}, {"name": "config.py"}]},
                {"name": "crud/", "description": "CRUD operations for database", "children": [{"name": "__init__.py"}, {"name": "base.py"}, {"name": "crud_user.py"}, {"name": "crud_backtest.py"}]},
                {"name": "db/", "description": "Database session management", "children": [{"name": "__init__.py"}, {"name": "supabase_client.py"}]},
                {"name": "models/", "description": "Pydantic models for validation & ORM", "children": [{"name": "__init__.py"}, {"name": "token.py"}, {"name": "user.py"}, {"name": "data.py"}, {"name": "strategy.py"}]},
                {"name": "schemas/", "description": "Pydantic schemas (can be merged with models)", "children": [{"name": "__init__.py"}, {"name": "user.py"}, {"name": "backtest.py"}]},
                {
                  "name": "services/", "description": "Business logic services",
                  "children": [
                    {"name": "__init__.py"},
                    {"name": "data_processor.py", "description": "Data cleaning, parsing, summary stats"},
                    {"name": "ai_code_generator.py", "description": "Interacts with AI for code generation"},
                    {"name": "backtest_executor.py", "description": "Executes backtest scripts securely"},
                    {"name": "auth_service.py", "description": "Handles authentication logic with Supabase"}
                  ]
                },
                {"name": "security/", "description": "Security related utilities", "children": [{"name": "__init__.py"}, {"name": "utils.py"}]},
                {"name": "worker/", "description": "(Optional) Celery or ARQ for background tasks", "children": [{"name": "__init__.py"}, {"name": "tasks.py"}]}
              ]
            },
            {"name": "tests/", "description": "Unit and integration tests"},
            {"name": ".env", "description": "Environment variables"},
            {"name": "requirements.txt"},
            {"name": "Dockerfile", "description": "For containerization"},
            {"name": "README.md"}
          ]
        },
        "componentResponsibilities": [
          {"component": "app/main.py", "responsibility": "Initializes FastAPI app, includes routers, middleware."},
          {"component": "app/api/v1/endpoints/auth.py", "responsibility": "Handles user registration, login, token generation."},
          {"component": "app/api/v1/endpoints/data.py", "responsibility": "Handles file uploads, yfinance data fetching, calls data_processor."},
          {"component": "app/api/v1/endpoints/strategy.py", "responsibility": "Receives NL strategy, calls ai_code_generator and backtest_executor, returns results."},
          {"component": "app/core/config.py", "responsibility": "Manages application settings and environment variables."},
          {"component": "app/crud/", "responsibility": "Functions for database interactions with Supabase."},
          {"component": "app/db/supabase_client.py", "responsibility": "Initializes and manages Supabase client for backend."},
          {"component": "app/models/ and app/schemas/", "responsibility": "Pydantic models for request/response validation and data structure."},
          {"component": "app/services/data_processor.py", "responsibility": "Uses Pandas for data parsing, cleaning, summary stats, initial viz data."},
          {"component": "app/services/ai_code_generator.py", "responsibility": "Constructs prompts, sends NL to AI API, receives Python code."},
          {"component": "app/services/backtest_executor.py", "responsibility": "Securely executes AI-generated Python code in a sandbox, computes metrics using backtesting libraries."},
          {"component": "app/services/auth_service.py", "responsibility": "Implements user authentication logic with Supabase."}
        ],
        "stateManagement": {
          "apiRequests": "Primarily stateless per request.",
          "requestSpecific": "Temporary state like DataFrames, strategy text, generated code (in memory during request).",
          "persistent": "Stored in Supabase: user accounts, strategy metadata, generated code, backtest results."
        },
        "serviceConnections": [
          "Responds to HTTP requests from the Frontend (Next.js).",
          "Makes HTTP requests to AI Service (OpenAI/Cursor AI).",
          "Uses `yfinance` library for market data.",
          "Interacts with Supabase via Supabase Python client for auth and data persistence.",
          "Utilizes backtesting libraries (e.g., `backtesting.py`, `bt`) within the `backtest_executor.py`."
        ]
      },
      "aiIntegration": {
        "name": "AI Integration (OpenAI API / Cursor AI)",
        "description": "Treated as an external service.",
        "role": "Converts natural language strategy descriptions into executable Python backtesting code.",
        "interaction": "Backend's `ai_code_generator.py` sends a crafted prompt to the AI API.",
        "output": "Returns a string containing Python code.",
        "considerations": "Prompt engineering is key for accuracy, safety, and compatibility."
      },
      "dataHandling": {
        "name": "Data Handling (Pandas, yfinance)",
        "yfinance": "Used in backend (`services/data_processor.py`) to fetch historical market data.",
        "pandas": "Used in `services/data_processor.py` for reading files, cleaning data, calculating indicators, summary stats, and preparing data for visualization/backtesting."
      },
      "databaseAndAuth": {
        "name": "Database and Auth (Supabase)",
        "description": "Provides PostgreSQL database, authentication, and other backend services.",
        "authentication": {
          "frontend": "Uses Supabase.js client for auth flow and session management.",
          "backend": "Validates JWTs. `auth.py` endpoint may interact with Supabase Admin SDK. `db/supabase_client.py` initializes client for backend."
        },
        "database": {
          "schemaConceptualTables": [
            {"name": "users", "description": "Standard Supabase auth users table."},
            {"name": "profiles", "description": "Extends users with app-specific info."},
            {"name": "historical_data_uploads", "description": "(Optional) `id`, `user_id`, `file_name`, `upload_timestamp`, `storage_path`, `data_hash`."},
            {"name": "strategies", "description": "`id`, `user_id`, `name`, `natural_language_description`, `generated_python_code`, `created_at`, `updated_at`."},
            {"name": "backtests", "description": "`id`, `strategy_id`, `user_id`, `data_source_info`, `execution_timestamp`, `status`."},
            {"name": "backtest_results", "description": "`id`, `backtest_id`, `total_return`, `max_drawdown`, `sharpe_ratio`, `win_rate`, `equity_curve_data` (JSON), `log_output`, `error_messages`."}
          ],
          "interaction": "Backend `crud` modules use Supabase Python client. Row Level Security (RLS) policies ensure data isolation."
        }
      },
      "keyConnectionsDataFlow": {
        "title": "Key Connections & Data Flow (Example: Running a Strategy)",
        "steps": [
          {
            "step": 1,
            "actor": "User Input (Frontend)",
            "actions": [
              "User uploads CSV or enters ticker/date range. Data sent to Backend.",
              "Backend processes data, returns summary/viz to Frontend.",
              "User enters NL strategy and clicks 'Run Backtest'. Frontend sends NL strategy and data reference to Backend."
            ]
          },
          {
            "step": 2,
            "actor": "Backend Processing",
            "actions": [
              "`strategy.py` endpoint receives request.",
              "Calls `ai_code_generator.py` which crafts prompt, sends to AI API, receives Python code.",
              "(Optional) Basic validation/sanitization of code.",
              "Stores NL strategy and generated code in Supabase.",
              "Calls `backtest_executor.py` with code and historical data."
            ]
          },
          {
            "step": 3,
            "actor": "Backtest Execution (Backend)",
            "actions": [
              "`backtest_executor.py` sets up sandbox, executes code using `backtesting.py`.",
              "Captures metrics and equity curve.",
              "Stores results in Supabase."
            ]
          },
          {
            "step": 4,
            "actor": "Results Display (Frontend)",
            "actions": [
              "Backend `strategy.py` returns backtest results.",
              "Frontend receives results.",
              "`ResultsDisplay.tsx` uses Plotly.js to render equity curve and display metrics."
            ]
          }
        ]
      }
    }
  }
}
