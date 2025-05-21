export default async function handler(req, res) {
  const resp = await fetch('http://localhost:8000/health');
  const data = await resp.json();
  res.status(200).json(data);
}
