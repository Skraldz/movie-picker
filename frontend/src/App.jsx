// Imports
import Sidebar from './Sidebar'
import PickMovie from './PickMovie'
import { useState } from 'react'

function App() {
  const [activePage, setActivePage] = useState('pick')
  return (
    <div>
      <h1>Movie Picker</h1>
      <Sidebar setActivePage={setActivePage} />
      {activePage === 'pick' && <PickMovie />}
      {activePage === 'add' && <p>Add Movie page</p>}
      {activePage === 'manage' && <p>Manage Movies page</p>}
    </div>
    
  )
}

export default App