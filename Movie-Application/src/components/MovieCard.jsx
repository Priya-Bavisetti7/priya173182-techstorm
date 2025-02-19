import React from 'react'

const MovieCard = ({ movie:
  { title, year, poster_path, imdbID }
}) => {
  return (
    <div className="movie-card">
      <img
        src={poster_path!=='N/A'?poster_path : '/no-movie.png'}
        alt={title}
      />

      <div className="mt-4">
        <h3>{title}</h3>

        <div className="content">
            <p className='year'>{year}</p>
            </div>
            </div>
            </div>
  )
}
export default MovieCard