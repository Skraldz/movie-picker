import { useState, useEffect } from 'react'

function PickMovie() {
    const [genres, setGenres] = useState([])
    const [selectedGenre, setSelectedGenre] = useState('')
    const [maxLength, setMaxLength] = useState('')
    const [releasedFrom, setReleasedFrom] = useState('')
    const [releasedTo, setReleasedTo] = useState('')
    const [selectedMovie, setSelectedMovie] = useState(null)
    const [tmdbDetails, setTmdbDetails] = useState(null)
    
        function pickMovie(){
            const url = new URL('http://192.168.5.10:8000/movies/pick')
            if (selectedGenre) url.searchParams.append('genre', selectedGenre)
            if (maxLength) url.searchParams.append('max_length', maxLength)
            if (releasedFrom) url.searchParams.append('released_from', releasedFrom)
            if (releasedTo) url.searchParams.append('released_to', releasedTo)
            fetch(url)
                .then(res => res.json())
                .then(data => setSelectedMovie(data))
        }

    useEffect(() => {
        fetch('http://192.168.5.10:8000/genres')
            .then(res => res.json())
            .then(data => setGenres(data))


    }, [])

    useEffect(() => {
        if (selectedMovie) {
        fetch(`http://192.168.5.10:8000/movies/${selectedMovie.tmdb_id}`)
            .then(res => res.json())
            .then(data => setTmdbDetails(data))
        }
    }, [selectedMovie])

    return(
        <div>
            <h2>Pick a Movie</h2>
            <select onChange={(e) => setSelectedGenre(e.target.value)}>
                <option value="">All genres</option>
                {genres.map(genre => (
                    <option key={genre.id} value={genre.genre}>{genre.genre}</option>
                ))}
            </select>
            <input placeholder="Search actors"/>
            <input placeholder="Max length" onChange={(e) => setMaxLength(e.target.value)}/> 
            <input placeholder="Released from" onChange={(e) => setReleasedFrom(e.target.value)}/>
            <input placeholder="Released to" onChange={(e) => setReleasedTo(e.target.value)}/>
            <button onClick={pickMovie}>Pick a Movie for me</button>

            {tmdbDetails && (
                <div>
                    <h3>{selectedMovie.title}</h3>
                    <img src={`https://image.tmdb.org/t/p/w500${tmdbDetails.movie_details.poster_path}`} />
                    <p>Description: {tmdbDetails.movie_details.overview}</p>
                </div>
            )}
        </div>
    )
}

export default PickMovie