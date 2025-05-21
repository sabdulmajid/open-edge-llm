import { useEffect, useState } from 'react';

export default function Home() {
  const [status, setStatus] = useState('');
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    fetch('/api/health')
      .then(res => res.json())
      .then(data => setStatus(data.status));
  }, []);

  const send = async () => {
    if (!input.trim()) return;
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });
    const data = await res.json();
    setMessages([...messages, { user: input, bot: data.answer }]);
    setInput('');
  };

  return (
    <div>
      <h1>OpenEdge Chat</h1>
      <p>Backend status: {status}</p>
      <div>
        {messages.map((m, idx) => (
          <div key={idx} style={{ marginBottom: '1em' }}>
            <strong>You:</strong> {m.user}<br />
            <strong>Bot:</strong> {m.bot}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Say something..."
      />
      <button onClick={send}>Send</button>
    </div>
  );
}
