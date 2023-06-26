import React, { useEffect, useState } from 'react'
import styless from './User.module.css'
import styles from './../Home/Home.module.css'
import { useParams } from 'react-router-dom'
import { $axios } from '../../api'

const User = () => {
  const {username} = useParams()
  const [games, setGames] = useState([])
  const [hightScores, setHightScores] = useState([])

  useEffect(() => {
    document.title = `User: ${username}`
    getData()
  }, [])

  const getData  = async () => {
    console.log(username)
    await $axios.get(`/users/${username}`)
      .then(res => {
        setHightScores(res.data.highscores)
        console.log(res.data.highscores)
        setGames(res.data.authoredGames)
      })
  }

  return (
    <div className='page'>
      <h2 className={styless.page__title}>{username}</h2>
      <h3 className={styless.page__title}>Authored Games</h3>
      <div className={styles.page__games}>
      {games? (
          <>
           {games.map(game => 
            <div className={styles.game} key={game.id}>
              <div className={styles.game__header}>
                <div className={styles.game__header__left}>
                  <a href={`/games/${game.slug}`} className={styles.title}>{game.title}</a>
                </div>                
                <span># scores submitted: {game.scores}</span>
              </div>
              <div className={styles.game__body}>
                <img src={`http://127.0.0.1:8000/${game.thumbnail}`} alt={game.title} />
                <p>{game.description}</p>
              </div>
            </div>
           )}
          </>
        ): (<p>Loading...</p>)}
      </div>
      <h3 className={styless.page__title}>Highscores per Game</h3>
      <div className={styless.highscores}>
        {hightScores? (
          <>
            {hightScores.map(score => 
              <div className={styless.highscore} key={score.id}>
                <h3>Game{score.game_version.game}</h3>
                <span>{score.score}</span>
              </div>  
            )}
          </>
        ): (<p>Loading...</p>)}
      </div>
    </div>
  )
}

export default User
