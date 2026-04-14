import { useState, useEffect } from "react";

function AddMovie() {
    const [title, setTitle] = useState('')
    const [query, setQuery] = useState(null)
    const [addedMovies, setAddedMovies] = useState([])

        function searchMovie(){
            const url = new URL('http://192.168.5.10:8000/search/')
            if (title) url.searchParams.append('query', title)
            fetch(url)
                .then(res => res.json())
                .then(data => setQuery(data))
        }

        function addMovie(id){
            const url = new URL(`http://192.168.5.10:8000/movies?tmdb_id=${id}`)
            fetch(url, {
                method: 'POST'
            })
        }

    useEffect(() => {
        fetch('http://192.168.5.10:8000/movies')
            .then(res => res.json())
            .then(data => setAddedMovies(data))
    }, [])

    return(
        <div>
            <h2>Add a Movie to the Database</h2>
            <input placeholder="Input title" onChange={(e) => setTitle(e.target.value)}/>
            <button onClick={searchMovie}>Search</button>

            {query && (
                <div>
                    {query.results.map(movie => {
                        const isAdded = addedMovies.some(dbMovie => dbMovie.tmdb_id === movie.id.toString())
                        return (
                            <div key={movie.id}>
                                <p>{movie.title}, {movie.release_date.slice(0, 4)}</p>
                                <img src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} />
                                <p>{movie.overview}</p>
                                <button disabled={isAdded} onClick={() => addMovie(movie.id)}>
                                    {isAdded ? 'Already Added' : 'Add Movie'}
                                </button>
                                <button>View on TMDB</button>
                            </div>
                        )
                    })}
                </div>
            )}
        </div>
    )
}

export default AddMovie