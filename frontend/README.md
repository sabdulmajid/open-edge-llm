# Front-end & APIs

FastAPI backend and a minimal Next.js frontend. Example: ask “Did I leave the stove on?” and the assistant fuses the last camera frame and sensor logs.

## Local development

1. Install dependencies inside `frontend/web` (or run `../../devops/setup_env.sh` from repo root):
   ```sh
   npm install
   ```
2. Run the Next.js dev server:
   ```sh
   npm run dev
   ```
3. Visit [http://localhost:3000](http://localhost:3000) to chat with the backend.

## Deploying to Vercel

1. Install the Vercel CLI if you haven't already:
   ```sh
   npm install -g vercel
   ```
2. Deploy from the `frontend/web` directory:
   ```sh
   cd frontend/web
   vercel --prod
   ```
   The CLI will output the deployment URL. Because this development environment has no network access, a live link cannot be provided here.
