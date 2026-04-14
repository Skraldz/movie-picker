// Imports
import Sidebar from './Sidebar'
import PickMovie from './PickMovie'
import AddMovie from './AddMovie'
import { useState } from 'react'

function App() {
  const [activePage, setActivePage] = useState('pick')
  return (
    <div>
      <h1>Movie Picker</h1>
      <Sidebar setActivePage={setActivePage} />
      {activePage === 'pick' && <PickMovie />}
      {activePage === 'add' && <AddMovie/>}
      {activePage === 'manage' && <p>Manage Movies page</p>}
    </div>
    
  )
}

export default App