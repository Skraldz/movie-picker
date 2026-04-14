function Sidebar({ setActivePage }) {
  return (
    <div>
        <h2>Menu</h2>
        <p onClick={() => setActivePage('pick')}>Pick Movie</p>
        <p onClick={() => setActivePage('add')}>Add Movie</p>
        <p onClick={() => setActivePage('manage')}>Manage Movies</p>
    </div>    
  )
}

export default Sidebar