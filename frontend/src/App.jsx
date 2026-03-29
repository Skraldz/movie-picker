import Sidebar from './Sidebar'
import { useState } from 'react'

function App() {
  const [activePage, setActivePage] = useState('pick')
  return (
    <div>
      <h1>Movie Picker</h1>
      <Sidebar />
    </div>
    
  )
}

export default App