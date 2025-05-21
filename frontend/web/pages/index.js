import { useEffect, useState } from 'react';

export default function Home() {
  const [status, setStatus] = useState('');
  useEffect(() => {
    fetch('/api/health').then(res => res.json()).then(data => setStatus(data.status));
  }, []);
  return <div>Backend status: {status}</div>;
}
