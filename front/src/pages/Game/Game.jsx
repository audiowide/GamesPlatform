import React, { useEffect, useState } from 'react'
import styles from './Game.module.css'
import { $axios } from '../../api'
import { useParams } from 'react-router-dom'

const Game = () => {
    const {slug} = useParams()
  const [game, setGame] = useState([])

  useEffect(() => {
    document.title = `${slug} `
    getData()
  }, [])

  const getData = async () => {
    $axios.get(`games/${slug}`)
      .then(res => {
        console.log(res.data)
        setGame(res.data)
        console.log(res.data)
      })
  }
  return (
    <div className='page'>
     {game ? (
        <>
        <h2>{game.title}</h2>
        <div className={styles.page__screen}>
            <img src={`http://127.0.0.1:8000/${game.thumbnail}`} alt={game.title} />
        </div>
        <div className="buttons">
            <div className={styles.buttons__left}>
                <h3>Top 10 Leaderboard</h3>
                
            </div>
            <div className={styles.description}>
                <h3>Description</h3>
                <p>{game.description}</p>
            </div>
        </div>
        </>
     ): (<p>loading..</p>)}
    </div>
  )
}

export default Game
