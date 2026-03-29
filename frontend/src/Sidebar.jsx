function Sidebar({ setActivePage }) {
  return (
    <div>
        <h4>Sidebar</h4>
        <p onClick={() => setActivePage('Pick')}>Pick Movie</p>
        <p onClick={() => setActivePage('Add')}>Add Movie</p>
        <p onClick={() => setActivePage('Manage')}>Manage Movies</p>
    </div>    
  )
}

export default Sidebar