{
  "mvpBuildPlan": {
    "title": "Granular Step-by-Step Plan for AI Quant Strategy Builder MVP",
    "phases": [
      {
        "phaseName": "Phase 0: Project Setup & Foundations",
        "tasks": [
          {
            "id": "0.1.1",
            "component": "Backend (FastAPI)",
            "task": "Initialize FastAPI project directory structure (`backend/`, `backend/app/`, etc.).",
            "start_condition": "No backend project directory.",
            "end_condition": "Basic FastAPI project folders created.",
            "test_verification": "Verify directory structure exists.",
            "focus": "Project scaffolding",
            "status": "completed"
          },
          {
            "id": "0.1.2",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/requirements.txt` and add `fastapi`, `uvicorn[standard]`, `pydantic`.",
            "start_condition": "No `requirements.txt` or core dependencies listed.",
            "end_condition": "`requirements.txt` exists with specified packages. Run `pip install -r requirements.txt`.",
            "test_verification": "Confirm packages are installable and listed.",
            "focus": "Dependency management"
          },
          {
            "id": "0.1.3",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/main.py` with a basic FastAPI app instance and a health check endpoint (`@app.get('/health')` returning `{\"status\": \"ok\"}`).",
            "start_condition": "No `main.py` or health check.",
            "end_condition": "`main.py` exists; `/health` endpoint returns 200 OK with JSON body.",
            "test_verification": "Run `uvicorn app.main:app --reload` and access `/health` via browser/curl.",
            "focus": "Basic server functionality"
          },
          {
            "id": "0.2.1",
            "component": "Frontend (Next.js)",
            "task": "Initialize Next.js project (`npx create-next-app@latest frontend --typescript --tailwind --eslint --app`). Select App Router.",
            "start_condition": "No frontend project directory.",
            "end_condition": "Next.js project `frontend/` created and dependencies installed.",
            "test_verification": "Run `npm run dev` in `frontend/` and see default Next.js page.",
            "focus": "Project scaffolding"
          },
          {
            "id": "0.2.2",
            "component": "Frontend (Next.js)",
            "task": "Install `plotly.js` and `react-plotly.js` (`npm install plotly.js react-plotly.js`).",
            "start_condition": "Plotly dependencies not installed.",
            "end_condition": "Plotly packages added to `package.json` and installed.",
            "test_verification": "Check `package.json` and `node_modules`.",
            "focus": "Charting library setup"
          },
          {
            "id": "0.2.3",
            "component": "Frontend (Next.js)",
            "task": "Modify `frontend/src/app/layout.tsx` and `frontend/src/app/page.tsx` for a basic app shell (e.g., a title and a placeholder main content area).",
            "start_condition": "Default Next.js page content.",
            "end_condition": "Custom basic layout rendered.",
            "test_verification": "View the page in browser, see custom title/content.",
            "focus": "Basic UI structure"
          },
          {
            "id": "0.3.1",
            "component": "Supabase",
            "task": "Create a new project in Supabase dashboard.",
            "start_condition": "No Supabase project for this MVP.",
            "end_condition": "Supabase project created and active.",
            "test_verification": "Log in to Supabase and see the project listed.",
            "focus": "Cloud DB/Auth setup"
          },
          {
            "id": "0.3.2",
            "component": "Supabase",
            "task": "Navigate to Project Settings > API in Supabase. Note down 'Project URL', 'anon public key', and 'service_role key'.",
            "start_condition": "API keys not yet recorded.",
            "end_condition": "Keys are copied and stored securely locally (e.g., in a password manager or temporary notes for next steps).",
            "test_verification": "Confirm the keys are accessible for configuration.",
            "focus": "Credentials retrieval"
          }
        ]
      },
      {
        "phaseName": "Phase 1: Authentication (Supabase)",
        "tasks": [
          {
            "id": "1.1.1",
            "component": "Backend (FastAPI)",
            "task": "Add `supabase-py` to `backend/requirements.txt` and install.",
            "start_condition": "Supabase Python client not in dependencies.",
            "end_condition": "`supabase-py` installed and in `requirements.txt`.",
            "test_verification": "Verify installation and `requirements.txt` update.",
            "focus": "Backend Supabase client"
          },
          {
            "id": "1.1.2",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/core/config.py` to load Supabase URL and service key from environment variables (e.g., `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`). Create a `.env` file and add these variables.",
            "start_condition": "No central config for Supabase keys.",
            "end_condition": "`config.py` loads keys; `.env` file populated (add `.env` to `.gitignore`).",
            "test_verification": "Print loaded keys in a test script to ensure they are read.",
            "focus": "Secure configuration"
          },
          {
            "id": "1.1.3",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/db/supabase_client.py` to initialize and provide a Supabase client instance using config from `config.py`.",
            "start_condition": "No Supabase client instance management.",
            "end_condition": "A function/singleton provides an initialized Supabase client.",
            "test_verification": "Instantiate client, check for connection errors (e.g., try a simple read if possible, or just ensure no init error).",
            "focus": "Supabase client initialization"
          },
          {
            "id": "1.1.4",
            "component": "Backend (FastAPI)",
            "task": "Create Pydantic models in `backend/app/schemas/user.py` for user signup (`UserCreate`) and login (`UserLogin`) requests, and a basic user response (`UserResponse`).",
            "start_condition": "No Pydantic models for auth.",
            "end_condition": "Pydantic models defined for email/password and user details.",
            "test_verification": "Models can be instantiated and validated.",
            "focus": "Data validation schemas"
          },
          {
            "id": "1.1.5",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/api/v1/endpoints/auth.py`. Implement a `/signup` endpoint using the Supabase client to register a user (email/password). Return user info or token from Supabase.",
            "start_condition": "No signup endpoint.",
            "end_condition": "`/signup` endpoint registers user in Supabase Auth and returns Supabase response.",
            "test_verification": "Call endpoint with new credentials using Postman/curl. Verify user in Supabase Dashboard > Authentication.",
            "focus": "User registration API"
          },
          {
            "id": "1.1.6",
            "component": "Backend (FastAPI)",
            "task": "Implement a `/login` endpoint in `auth.py` using Supabase client to sign in a user (email/password). Return session/token from Supabase.",
            "start_condition": "No login endpoint.",
            "end_condition": "`/login` endpoint authenticates user and returns Supabase session/token.",
            "test_verification": "Call endpoint with valid/invalid credentials used in signup. Verify token is returned on success.",
            "focus": "User login API"
          },
          {
            "id": "1.1.7",
            "component": "Backend (FastAPI)",
            "task": "Implement a dependency in `backend/app/security/utils.py` to get current user from Supabase JWT. Create a basic protected endpoint (e.g., `/users/me`) in `auth.py` that uses this dependency.",
            "start_condition": "No token validation or protected route.",
            "end_condition": "Protected endpoint returns user info if valid token provided, 401 otherwise.",
            "test_verification": "Call `/users/me` with and without a valid JWT (obtained from login).",
            "focus": "API protection (JWT)"
          },
          {
            "id": "1.1.8",
            "component": "Backend (FastAPI)",
            "task": "Add the auth router to `backend/app/main.py`.",
            "start_condition": "Auth endpoints not exposed.",
            "end_condition": "`/api/v1/auth/signup`, `/api/v1/auth/login`, `/api/v1/users/me` are accessible.",
            "test_verification": "Retest endpoints via their full path.",
            "focus": "API routing"
          },
          {
            "id": "1.2.1",
            "component": "Frontend (Next.js)",
            "task": "Install `@supabase/supabase-js` (`npm install @supabase/supabase-js`).",
            "start_condition": "Supabase JS client not installed.",
            "end_condition": "Package added to `package.json` and installed.",
            "test_verification": "Check `package.json`.",
            "focus": "Frontend Supabase client"
          },
          {
            "id": "1.2.2",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/lib/supabaseClient.ts` to initialize and export Supabase JS client using Project URL and anon key (from `.env.local`). Create `.env.local` and add `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`.",
            "start_condition": "No frontend Supabase client setup.",
            "end_condition": "`supabaseClient.ts` exports client; `.env.local` configured (add to `.gitignore`).",
            "test_verification": "Import client in a page, check if it initializes without error.",
            "focus": "Client-side Supabase init"
          },
          {
            "id": "1.2.3",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/app/(auth)/signup/page.tsx` with a form (email, password inputs, submit button).",
            "start_condition": "No signup page/form.",
            "end_condition": "Signup form renders with inputs.",
            "test_verification": "Navigate to `/signup`, view form.",
            "focus": "Signup UI"
          },
          {
            "id": "1.2.4",
            "component": "Frontend (Next.js)",
            "task": "Implement client-side signup logic in `signup/page.tsx` to call `supabase.auth.signUp()` using the imported Supabase client.",
            "start_condition": "Signup form is static.",
            "end_condition": "Form submission calls Supabase auth; displays success (check email) or error message.",
            "test_verification": "Use form to signup a new user. Verify user in Supabase Dashboard (may require email confirmation setup in Supabase).",
            "focus": "Client-side signup logic"
          },
          {
            "id": "1.2.5",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/app/(auth)/login/page.tsx` with a form (email, password inputs, submit button).",
            "start_condition": "No login page/form.",
            "end_condition": "Login form renders with inputs.",
            "test_verification": "Navigate to `/login`, view form.",
            "focus": "Login UI"
          },
          {
            "id": "1.2.6",
            "component": "Frontend (Next.js)",
            "task": "Implement client-side login logic in `login/page.tsx` to call `supabase.auth.signInWithPassword()`.",
            "start_condition": "Login form is static.",
            "end_condition": "Form submission calls Supabase auth; stores session (e.g., Supabase handles this); displays success/error.",
            "test_verification": "Use form to login with previously signed-up user. Check browser local storage for Supabase session.",
            "focus": "Client-side login logic"
          },
          {
            "id": "1.2.7",
            "component": "Frontend (Next.js)",
            "task": "Create an AuthContext (`frontend/src/contexts/AuthContext.tsx`) to manage user session state and provide it globally. Listen to `supabase.auth.onAuthStateChange`.",
            "start_condition": "No global auth state.",
            "end_condition": "AuthContext created and wrapped around app layout; user state updates on auth events.",
            "test_verification": "Log in/out, observe context state changes via React DevTools or console logs.",
            "focus": "Global auth state"
          },
          {
            "id": "1.2.8",
            "component": "Frontend (Next.js)",
            "task": "Create a LogoutButton component that calls `supabase.auth.signOut()` and clears user from AuthContext.",
            "start_condition": "No logout functionality.",
            "end_condition": "Logout button signs out user, clears session.",
            "test_verification": "Click logout, verify user is logged out (context updates, local storage cleared).",
            "focus": "Logout functionality"
          },
          {
            "id": "1.2.9",
            "component": "Frontend (Next.js)",
            "task": "Create a sample protected page (e.g., `frontend/src/app/dashboard/page.tsx`). Redirect to `/login` if user is not authenticated (use AuthContext).",
            "start_condition": "No protected route example.",
            "end_condition": "`/dashboard` is accessible only if logged in.",
            "test_verification": "Attempt to access `/dashboard` when logged out (redirects to login) and logged in (shows page).",
            "focus": "Route protection"
          }
        ]
      },
      {
        "phaseName": "Phase 2: Data Input - File Upload",
        "tasks": [
          {
            "id": "2.1.1",
            "component": "Backend (FastAPI)",
            "task": "Add `python-multipart` to `backend/requirements.txt` for form data/file uploads and install.",
            "start_condition": "File upload dependency not present.",
            "end_condition": "`python-multipart` installed and in `requirements.txt`.",
            "test_verification": "Verify installation.",
            "focus": "File upload dependency"
          },
          {
            "id": "2.1.2",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/api/v1/endpoints/data.py`. Implement a `/upload/csv` endpoint accepting `UploadFile` from `fastapi`. Initially, just return filename and content type.",
            "start_condition": "No CSV upload endpoint.",
            "end_condition": "Endpoint receives file, returns basic metadata.",
            "test_verification": "Send a CSV file via Postman (form-data). Verify response.",
            "focus": "Basic CSV upload API"
          },
          {
            "id": "2.1.3",
            "component": "Backend (FastAPI)",
            "task": "Add `pandas` to `backend/requirements.txt` and install.",
            "start_condition": "Pandas not in dependencies.",
            "end_condition": "Pandas installed and in `requirements.txt`.",
            "test_verification": "Verify installation.",
            "focus": "Data manipulation library"
          },
          {
            "id": "2.1.4",
            "component": "Backend (FastAPI)",
            "task": "In `/upload/csv` endpoint, read the uploaded CSV file into a Pandas DataFrame. Return the first 5 rows as JSON.",
            "start_condition": "Endpoint doesn't process CSV content.",
            "end_condition": "Endpoint parses CSV to DataFrame, returns head as JSON.",
            "test_verification": "Upload a sample CSV. Verify JSON response contains first 5 rows.",
            "focus": "CSV parsing"
          },
          {
            "id": "2.1.5",
            "component": "Backend (FastAPI)",
            "task": "Implement `/upload/excel` endpoint in `data.py` accepting `UploadFile`. Read using `pd.read_excel()`. Return first 5 rows as JSON.",
            "start_condition": "No Excel upload endpoint.",
            "end_condition": "Endpoint parses Excel to DataFrame, returns head as JSON.",
            "test_verification": "Upload a sample XLSX file. Verify JSON response contains first 5 rows. (Requires `openpyxl` or other engine, add to `requirements.txt`).",
            "focus": "Excel parsing"
          },
          {
            "id": "2.1.6",
            "component": "Backend (FastAPI)",
            "task": "Add the data router to `backend/app/main.py` (prefix `/api/v1/data`). Protect these endpoints (require authentication).",
            "start_condition": "Data endpoints not exposed or protected.",
            "end_condition": "`/api/v1/data/upload/csv` and `/api/v1/data/upload/excel` are accessible and require JWT.",
            "test_verification": "Test endpoints with and without valid token.",
            "focus": "API routing & security"
          },
          {
            "id": "2.2.1",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/data-input/FileUpload.tsx` with a file input (`<input type='file'>`) and an upload button.",
            "start_condition": "No file upload UI component.",
            "end_condition": "Component renders file input and button.",
            "test_verification": "Add component to `dashboard/page.tsx` and view in browser.",
            "focus": "File input UI"
          },
          {
            "id": "2.2.2",
            "component": "Frontend (Next.js)",
            "task": "In `FileUpload.tsx`, manage selected file in component state. On button click, create `FormData` and post to `/api/v1/data/upload/csv` (if CSV) or `/api/v1/data/upload/excel` (if Excel). Include auth token in request headers.",
            "start_condition": "File input is static.",
            "end_condition": "File selected is sent to appropriate backend endpoint. Display success/error message from backend.",
            "test_verification": "Upload CSV/Excel. Verify backend receives it and frontend shows status. Check network tab for token.",
            "focus": "Client-side file send"
          },
          {
            "id": "2.2.3",
            "component": "Frontend (Next.js)",
            "task": "In `FileUpload.tsx`, display the first 5 rows of data returned by the backend in a simple table or preformatted text block after successful upload.",
            "start_condition": "Backend response not displayed.",
            "end_condition": "Data preview (head of DataFrame) shown on UI.",
            "test_verification": "Upload file, verify preview data matches expected.",
            "focus": "Data preview UI"
          }
        ]
      },
      {
        "phaseName": "Phase 3: Data Input - Market Data Fetch (yfinance)",
        "tasks": [
          {
            "id": "3.1.1",
            "component": "Backend (FastAPI)",
            "task": "Add `yfinance` to `backend/requirements.txt` and install.",
            "start_condition": "yfinance not in dependencies.",
            "end_condition": "yfinance installed and in `requirements.txt`.",
            "test_verification": "Verify installation.",
            "focus": "Market data library"
          },
          {
            "id": "3.1.2",
            "component": "Backend (FastAPI)",
            "task": "Create Pydantic model in `backend/app/schemas/data.py` for ticker fetch request (`TickerRequest` with ticker, start_date, end_date).",
            "start_condition": "No schema for ticker fetch.",
            "end_condition": "Pydantic model defined.",
            "test_verification": "Model can be instantiated.",
            "focus": "Request validation schema"
          },
          {
            "id": "3.1.3",
            "component": "Backend (FastAPI)",
            "task": "Implement `/fetch/ticker` (POST) endpoint in `data.py`. Use `yfinance.download()` to fetch data. Return first 5 rows as JSON. Protect endpoint.",
            "start_condition": "No ticker fetch endpoint.",
            "end_condition": "Endpoint fetches data using yfinance, returns head as JSON, requires auth.",
            "test_verification": "Call with valid ticker/dates (e.g., AAPL, 2023-01-01, 2023-01-10) via Postman with token. Verify response.",
            "focus": "Ticker data fetching API"
          },
          {
            "id": "3.2.1",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/data-input/TickerForm.tsx` with inputs for ticker, start date, end date, and a fetch button.",
            "start_condition": "No ticker input UI component.",
            "end_condition": "Component renders form elements.",
            "test_verification": "Add to `dashboard/page.tsx` and view in browser.",
            "focus": "Ticker input UI"
          },
          {
            "id": "3.2.2",
            "component": "Frontend (Next.js)",
            "task": "In `TickerForm.tsx`, on button click, send form data as JSON to `/api/v1/data/fetch/ticker`. Include auth token. Display success/error.",
            "start_condition": "Ticker form is static.",
            "end_condition": "Data sent to backend; status displayed.",
            "test_verification": "Submit form. Verify backend receives request and frontend shows status.",
            "focus": "Client-side ticker fetch"
          },
          {
            "id": "3.2.3",
            "component": "Frontend (Next.js)",
            "task": "In `TickerForm.tsx`, display the first 5 rows of data returned by the backend in a simple table or preformatted text block after successful fetch.",
            "start_condition": "Backend response not displayed.",
            "end_condition": "Data preview (head of DataFrame) shown on UI.",
            "test_verification": "Fetch data, verify preview.",
            "focus": "Data preview UI"
          }
        ]
      },
      {
        "phaseName": "Phase 4: Data Processing & Basic Visualization",
        "tasks": [
          {
            "id": "4.1.1",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/services/data_processor.py`. Add a function `standardize_data(df: pd.DataFrame) -> pd.DataFrame` to ensure common column names (e.g., 'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'). Handle potential case variations and common alternatives (e.g. 'Date' for 'Timestamp').",
            "start_condition": "No data standardization logic.",
            "end_condition": "Function standardizes columns of a DataFrame.",
            "test_verification": "Unit test with DataFrames having varied column names.",
            "focus": "Data column standardization"
          },
          {
            "id": "4.1.2",
            "component": "Backend (FastAPI)",
            "task": "Integrate `standardize_data` function into `/upload/csv`, `/upload/excel`, and `/fetch/ticker` endpoints after data is loaded into DataFrame. The returned 5 rows should reflect standardized columns.",
            "start_condition": "Endpoints return raw column names.",
            "end_condition": "Endpoints return data with standardized column names.",
            "test_verification": "Test all data input endpoints; verify column names in response.",
            "focus": "Standardization integration"
          },
          {
            "id": "4.1.3",
            "component": "Backend (FastAPI)",
            "task": "In `data_processor.py`, add function `get_summary_statistics(df: pd.DataFrame) -> dict` to calculate mean, median, std, min, max for 'Close' and 'Volume'.",
            "start_condition": "No summary statistics calculation.",
            "end_condition": "Function returns dictionary of summary stats.",
            "test_verification": "Unit test with a sample DataFrame.",
            "focus": "Summary statistics calculation"
          },
          {
            "id": "4.1.4",
            "component": "Backend (FastAPI)",
            "task": "Modify all data input endpoints to include summary statistics in their response, alongside the data preview.",
            "start_condition": "Endpoints don't return summary stats.",
            "end_condition": "Endpoints' responses include a `summary_statistics` field.",
            "test_verification": "Test data input endpoints; verify stats in response.",
            "focus": "Exposing summary stats"
          },
          {
            "id": "4.1.5",
            "component": "Backend (FastAPI)",
            "task": "In `data_processor.py`, add function `calculate_moving_average(df: pd.DataFrame, window: int, column: str = 'Close') -> pd.Series`.",
            "start_condition": "No moving average calculation.",
            "end_condition": "Function returns a Series with moving average values.",
            "test_verification": "Unit test with sample DataFrame and window (e.g., 50).",
            "focus": "Moving average calculation"
          },
          {
            "id": "4.1.6",
            "component": "Backend (FastAPI)",
            "task": "Modify data input endpoints: after standardization, calculate 50-day MA. Return the full DataFrame (or a larger chunk, e.g., 200 rows if too large) as JSON suitable for Plotly (e.g., `{ 'timestamp': [...], 'close': [...], 'ma50': [...] }`) instead of just 5 rows. Include this in a `chart_data` field in the response.",
            "start_condition": "Endpoints return only 5 rows, no MA.",
            "end_condition": "Endpoints return expanded data with MA50, formatted for charting.",
            "test_verification": "Test endpoints; verify `chart_data` field with expected arrays.",
            "focus": "Preparing data for charts"
          },
          {
            "id": "4.2.1",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/data-summary/DataSummary.tsx` to display key-value pairs. In `dashboard/page.tsx`, pass the `summary_statistics` from API response to this component.",
            "start_condition": "Summary stats not displayed.",
            "end_condition": "Component displays summary statistics.",
            "test_verification": "Upload/fetch data; verify stats displayed correctly.",
            "focus": "Summary stats UI"
          },
          {
            "id": "4.2.2",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/charts/PriceChart.tsx` using `react-plotly.js`. It should accept data props (timestamps, close prices, MA50 prices).",
            "start_condition": "No price chart component.",
            "end_condition": "Component can render a Plotly chart with price and MA lines given data.",
            "test_verification": "Pass static sample data to component; verify chart renders.",
            "focus": "Price chart component"
          },
          {
            "id": "4.2.3",
            "component": "Frontend (Next.js)",
            "task": "In `dashboard/page.tsx`, pass the `chart_data` from API response to `PriceChart.tsx` to display the Close price and MA50.",
            "start_condition": "Price chart not displaying live data.",
            "end_condition": "Chart displays data from backend.",
            "test_verification": "Upload/fetch data; verify price and MA50 lines on chart.",
            "focus": "Live data price chart"
          },
          {
            "id": "4.2.4",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/charts/VolumeChart.tsx` using `react-plotly.js` to display volume as a bar chart. Pass relevant `chart_data` (timestamps, volume) to it.",
            "start_condition": "No volume chart.",
            "end_condition": "Volume chart displays data from backend.",
            "test_verification": "Upload/fetch data; verify volume chart.",
            "focus": "Volume chart UI"
          }
        ]
      },
      {
        "phaseName": "Phase 5: NL Strategy Input & AI Code Generation",
        "tasks": [
          {
            "id": "5.1.1",
            "component": "AI Integration (OpenAI)",
            "task": "Sign up for OpenAI API access and obtain an API key.",
            "start_condition": "No OpenAI API key.",
            "end_condition": "API key obtained and stored securely.",
            "test_verification": "Key is available for backend configuration.",
            "focus": "AI service access"
          },
          {
            "id": "5.1.2",
            "component": "Backend (FastAPI)",
            "task": "Add `openai` to `backend/requirements.txt` and install. Configure OpenAI API key in `backend/app/core/config.py` (from environment variable `OPENAI_API_KEY`). Add to `.env`.",
            "start_condition": "OpenAI client/key not configured.",
            "end_condition": "OpenAI client installable; API key configured.",
            "test_verification": "Verify key loading in `config.py`.",
            "focus": "AI client setup"
          },
          {
            "id": "5.1.3",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/services/ai_code_generator.py`. Implement a function `generate_code_from_nl(nl_strategy: str) -> str` that initializes OpenAI client and makes a simple chat completion request (e.g., `gpt-3.5-turbo`) with a prompt like: \"Convert the following natural language trading strategy into Python code for the 'backtesting.py' library. Strategy: [nl_strategy]\". Return the generated code string.",
            "start_condition": "No AI code generation logic.",
            "end_condition": "Function calls OpenAI API and returns text response.",
            "test_verification": "Directly call function with a test string (e.g., \"Buy AAPL when price is above 150\"). Verify a code-like string is returned (actual correctness not critical yet).",
            "focus": "Basic AI interaction"
          },
          {
            "id": "5.1.4",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/api/v1/endpoints/strategy.py`. Implement a `/generate-code` (POST) endpoint accepting JSON with `nl_description: str`. Call `generate_code_from_nl` and return the result. Protect endpoint.",
            "start_condition": "No strategy code generation API.",
            "end_condition": "Endpoint takes NL, returns AI-generated code, requires auth.",
            "test_verification": "Call endpoint via Postman with NL text. Verify AI response.",
            "focus": "Code generation API"
          },
          {
            "id": "5.1.5",
            "component": "Backend (FastAPI)",
            "task": "Add strategy router to `backend/app/main.py` (prefix `/api/v1/strategy`).",
            "start_condition": "Strategy endpoint not exposed.",
            "end_condition": "`/api/v1/strategy/generate-code` is accessible.",
            "test_verification": "Retest endpoint.",
            "focus": "API routing"
          },
          {
            "id": "5.2.1",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/strategy-input/StrategyInput.tsx` with a textarea for NL strategy and a \"Generate Code\" button.",
            "start_condition": "No NL input UI.",
            "end_condition": "Component renders textarea and button.",
            "test_verification": "Add to `dashboard/page.tsx` and view.",
            "focus": "NL input UI"
          },
          {
            "id": "5.2.2",
            "component": "Frontend (Next.js)",
            "task": "In `StrategyInput.tsx`, on button click, send textarea content to `/api/v1/strategy/generate-code`. Include auth token. Display returned code in a `<pre>` tag or similar.",
            "start_condition": "NL input is static.",
            "end_condition": "NL sent to backend; generated code displayed.",
            "test_verification": "Enter NL, click button. Verify backend called, code displayed on UI.",
            "focus": "Client-side code generation trigger"
          }
        ]
      },
      {
        "phaseName": "Phase 6: Backtest Execution",
        "tasks": [
          {
            "id": "6.1.1",
            "component": "Backend (FastAPI)",
            "task": "Add `backtesting.py` to `backend/requirements.txt` and install.",
            "start_condition": "Backtesting library not in dependencies.",
            "end_condition": "`backtesting.py` installed and in `requirements.txt`.",
            "test_verification": "Verify installation.",
            "focus": "Backtesting library"
          },
          {
            "id": "6.1.2",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/services/backtest_executor.py`. Implement a function `run_backtest(code_string: str, data: pd.DataFrame) -> dict`. Inside, use `exec(code_string, globals_dict, locals_dict)` to define the strategy. Then instantiate `backtesting.Backtest` with data and the executed strategy class. Run it and extract basic stats (e.g., `bt.run()['Return [%]']`, `bt.run()['Max. Drawdown [%]']`, `bt.run()._equity_curve`). Return these stats.",
            "start_condition": "No backtest execution logic.",
            "end_condition": "Function executes code, runs backtest, returns results dictionary.",
            "test_verification": "Manually create a simple valid `backtesting.py` strategy string and a sample DataFrame. Call `run_backtest`. Verify stats are returned. Handle potential errors from `exec` or `backtesting.py` gracefully (e.g. try-except).",
            "focus": "Core backtest execution"
          },
          {
            "id": "6.1.3",
            "component": "Backend (FastAPI)",
            "task": "(Security MVP) In `run_backtest`, define a `restricted_globals` dictionary for `exec()`. Allow `pandas`, `backtesting.Strategy`, and common math functions. Deny `__import__`, `eval`, `open`, `os`, `sys` etc.",
            "start_condition": "`exec` uses default globals or minimal restriction.",
            "end_condition": "`exec` uses a more restricted set of globals.",
            "test_verification": "Attempt to execute code with a forbidden import/function (e.g., `import os`). Verify it fails with an error.",
            "focus": "Basic `exec` sandboxing"
          },
          {
            "id": "6.1.4",
            "component": "Backend (FastAPI)",
            "task": "Create Pydantic models in `backend/app/schemas/strategy.py` for backtest request (`BacktestRequest` with `python_code: str` and a way to identify/pass data) and response (`BacktestResponse` with metrics and equity curve).",
            "start_condition": "No schemas for backtest execution.",
            "end_condition": "Pydantic models defined.",
            "test_verification": "Models can be instantiated.",
            "focus": "Backtest API schemas"
          },
          {
            "id": "6.1.5",
            "component": "Backend (FastAPI)",
            "task": "Implement `/run-backtest` (POST) endpoint in `strategy.py`. It should accept `python_code`. For data, it will need to re-fetch/re-load based on parameters passed from frontend representing the current dataset (MVP: pass ticker/dates or filename again). Call `run_backtest` and return results. Protect endpoint.",
            "start_condition": "No backtest execution API.",
            "end_condition": "Endpoint takes code, gets data, runs backtest, returns results, requires auth.",
            "test_verification": "Call endpoint with AI-generated code (from previous phase) and relevant data parameters. Verify backtest results in response.",
            "focus": "Backtest execution API"
          },
          {
            "id": "6.2.1",
            "component": "Frontend (Next.js)",
            "task": "In `dashboard/page.tsx` (or a new component), add a \"Run Backtest\" button, visible after code is generated.",
            "start_condition": "No UI to trigger backtest.",
            "end_condition": "Button rendered.",
            "test_verification": "View UI after code generation.",
            "focus": "Backtest trigger UI"
          },
          {
            "id": "6.2.2",
            "component": "Frontend (Next.js)",
            "task": "On \"Run Backtest\" click, send the generated Python code and current data context (e.g., ticker/dates if yfinance data, or original filename if uploaded data - these params need to be stored in frontend state from data input phase) to `/api/v1/strategy/run-backtest`. Include auth token.",
            "start_condition": "Backtest button is static.",
            "end_condition": "Request sent to backend with code and data context.",
            "test_verification": "Click button. Verify backend receives code and data context. Frontend shows loading/status.",
            "focus": "Client-side backtest trigger"
          }
        ]
      },
      {
        "phaseName": "Phase 7: Results Visualization",
        "tasks": [
          {
            "id": "7.1.1",
            "component": "Frontend (Next.js)",
            "task": "Create `frontend/src/components/results/ResultsDisplay.tsx`. It should display text for Total Return, Max Drawdown, Win Rate, Sharpe Ratio.",
            "start_condition": "No dedicated results display component.",
            "end_condition": "Component can render placeholder text for metrics.",
            "test_verification": "Add to `dashboard/page.tsx` and view.",
            "focus": "Metrics display UI structure"
          },
          {
            "id": "7.1.2",
            "component": "Frontend (Next.js)",
            "task": "In `ResultsDisplay.tsx`, use `react-plotly.js` to render an equity curve chart. It should accept equity curve data (e.g., an array of values or {x: dates, y: values}).",
            "start_condition": "Results component doesn't have chart.",
            "end_condition": "Component can render a Plotly chart for equity curve.",
            "test_verification": "Pass static sample equity curve data; verify chart renders.",
            "focus": "Equity curve chart structure"
          },
          {
            "id": "7.1.3",
            "component": "Frontend (Next.js)",
            "task": "In `dashboard/page.tsx`, after receiving response from `/run-backtest`, pass the metrics and equity curve data to `ResultsDisplay.tsx`.",
            "start_condition": "Backend results not shown on UI.",
            "end_condition": "Metrics and equity curve chart are displayed with live backtest data.",
            "test_verification": "Run a full backtest. Verify metrics and chart are correctly displayed.",
            "focus": "Live results display"
          }
        ]
      },
      {
        "phaseName": "Phase 8: Basic Persistence (Supabase)",
        "tasks": [
          {
            "id": "8.1.1",
            "component": "Supabase",
            "task": "In Supabase Studio SQL Editor, create `strategies` table: `id (uuid, pk)`, `user_id (uuid, fk to auth.users)`, `natural_language_description (text)`, `generated_python_code (text)`, `created_at (timestamptz, default now())`.",
            "start_condition": "No `strategies` table.",
            "end_condition": "`strategies` table created with RLS enabled (default). Add basic RLS policy for select/insert by authenticated user matching `user_id`.",
            "test_verification": "Verify table structure and RLS policies in Supabase Studio.",
            "focus": "Strategy persistence schema"
          },
          {
            "id": "8.1.2",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/crud/crud_strategy.py`. Implement `create_strategy(db: Client, user_id: str, nl_description: str, generated_code: str) -> dict` to insert into Supabase `strategies` table.",
            "start_condition": "No CRUD function for strategies.",
            "end_condition": "Function inserts strategy data into Supabase.",
            "test_verification": "Unit test function with mock Supabase client or by calling it with a real client and verifying DB entry.",
            "focus": "Save strategy logic"
          },
          {
            "id": "8.1.3",
            "component": "Backend (FastAPI)",
            "task": "Modify `/strategy/generate-code` endpoint: after successfully generating code, call `create_strategy` to save the NL and generated code, associating with `current_user.id`.",
            "start_condition": "Generated strategies not saved.",
            "end_condition": "NL strategy and generated code persisted to DB.",
            "test_verification": "Call `/generate-code`. Verify new entry in `strategies` table in Supabase.",
            "focus": "Persist generated strategy"
          },
          {
            "id": "8.1.4",
            "component": "Supabase",
            "task": "Create `backtest_results` table: `id (uuid, pk)`, `strategy_id (uuid, fk to strategies)`, `user_id (uuid, fk to auth.users)`, `executed_at (timestamptz, default now())`, `total_return (float)`, `max_drawdown (float)`, `sharpe_ratio (float)`, `win_rate (float)`, `equity_curve_data (jsonb)`.",
            "start_condition": "No `backtest_results` table.",
            "end_condition": "`backtest_results` table created with RLS. Add RLS policies.",
            "test_verification": "Verify table structure and RLS policies.",
            "focus": "Backtest results schema"
          },
          {
            "id": "8.1.5",
            "component": "Backend (FastAPI)",
            "task": "Create `backend/app/crud/crud_backtest.py`. Implement `create_backtest_result(db: Client, user_id: str, strategy_id: str, results: dict)` to insert into `backtest_results`.",
            "start_condition": "No CRUD function for backtest results.",
            "end_condition": "Function inserts backtest result data.",
            "test_verification": "Unit test function.",
            "focus": "Save backtest result logic"
          },
          {
            "id": "8.1.6",
            "component": "Backend (FastAPI)",
            "task": "Modify `/strategy/run-backtest` endpoint: after successful backtest, call `create_backtest_result`. Requires strategy_id (frontend might need to pass ID of generated strategy if user runs backtest on a previously generated one, or backend looks up latest for user). For MVP, assume it's the latest strategy generated for user or pass the `generated_code`'s `strategy_id` if available. Store `user_id` also.",
            "start_condition": "Backtest results not saved.",
            "end_condition": "Backtest results persisted to DB.",
            "test_verification": "Run backtest. Verify new entry in `backtest_results` table.",
            "focus": "Persist backtest results"
          }
        ]
      },
      {
        "phaseName": "Phase 9: MVP Polish & Testing",
        "tasks": [
          {
            "id": "9.1.1",
            "component": "Frontend (Next.js)",
            "task": "Implement basic try-catch blocks around API calls in frontend components. Display user-friendly error messages (e.g., using a toast notification or a dedicated error display area).",
            "start_condition": "Rudimentary or no error handling.",
            "end_condition": "Common API errors show clear messages to user.",
            "test_verification": "Simulate backend errors (e.g., stop backend server, return 500 from an endpoint). Verify frontend handles gracefully.",
            "focus": "Frontend error handling"
          },
          {
            "id": "9.1.2",
            "component": "Backend (FastAPI)",
            "task": "Ensure all backend endpoints use FastAPI's HTTPException for errors and return appropriate HTTP status codes (400, 401, 403, 404, 500).",
            "start_condition": "Inconsistent error responses.",
            "end_condition": "Standardized and informative error responses from API.",
            "test_verification": "Send various invalid requests (bad data, no auth, non-existent resource). Check status codes and error messages.",
            "focus": "Backend error handling"
          },
          {
            "id": "9.1.3",
            "component": "Frontend (Next.js)",
            "task": "Add loading indicators (spinners, text messages) for API calls: data fetch/upload, code generation, backtest execution.",
            "start_condition": "No visual feedback during API calls.",
            "end_condition": "UI shows loading state during operations.",
            "test_verification": "Perform each long operation; verify loading indicators appear and disappear.",
            "focus": "User experience (loading)"
          },
          {
            "id": "9.1.4",
            "component": "Frontend (Next.js)",
            "task": "Review and refine the main UI flow on `dashboard/page.tsx`. Ensure components (Data Input, Strategy Input, Results) are logically arranged and appear/update based on application state.",
            "start_condition": "Components may be disjointed.",
            "end_condition": "A cohesive user journey on the dashboard page.",
            "test_verification": "Manually walk through typical user interactions. Check for clarity and ease of use.",
            "focus": "UI/UX flow"
          },
          {
            "id": "9.1.5",
            "component": "System-Wide",
            "task": "Conduct a full end-to-end test of the MVP: Signup, Login, Upload CSV, View Data/Chart, Input NL Strategy, Generate Code, Run Backtest, View Results. Verify data persistence in Supabase for strategies and backtest results.",
            "start_condition": "Individual features tested, but not full flow.",
            "end_condition": "Full MVP user story successfully completed and data persisted.",
            "test_verification": "Execute all steps of the user story without errors. Check Supabase tables for correct entries.",
            "focus": "End-to-end MVP validation"
          }
        ]
      }
    ]
  }
}
