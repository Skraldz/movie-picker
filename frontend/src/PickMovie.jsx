import { useState, useEffect } from 'react'

function PickMovie() {
    const [genres, setGenres] = useState([])

    useEffect(() => {
        fetch('http://192.168.5.10:8000/genres')
            .then(res => res.json())
            .then(data => setGenres(data))
    }, [])
    return(
        <div>
            <h2>Pick a Movie</h2>
            <select>
                <option value="">All genres</option>
                {genres.map(genre => (
                    <option key={genre.id} value={genre.genre}>{genre.genre}</option>
                ))}
            </select>
            <input placeholder="Search actors"/>
        </div>
    )
}

export default PickMovie