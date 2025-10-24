import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [currentCount, setCurrentCount] = useState(null)

  async function fetchCount() {
    try {
      const res = await fetch('http://localhost:3000/api/count')
      if (!res.ok) throw new Error('Failed to fetch count')
      const json = await res.json()
      setCurrentCount(json.currentCount)
    } catch (error) {
      console.error('Error fetching count:', error)
      setCurrentCount(null)
    }
  }

  function incrementBackendCount() {
    fetch('http://localhost:3000/api/increment', { method: 'POST' })
      .then(res => res.json())
      .then(json => setCurrentCount(json.currentCount))
      .catch(error => console.error('Error incrementing count:', error));
  }

  useEffect(() => {
    fetchCount();
  }, [])

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={incrementBackendCount}>
          count is {currentCount !== null ? currentCount : 'Loading...'}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App