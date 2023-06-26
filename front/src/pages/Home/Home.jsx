import { useEffect, useState } from 'react'
import styles from './Home.module.css'
import { $axios } from '../../api'
import { useAuth } from '../../hooks/useAuth'

const Home = () => {
  const [data, setData] = useState([])
  const [games, setGames] = useState([])
  const {name} = useAuth()

  useEffect(() => {
    getData()
  }, [])

  const getData = async () => {
    await $axios.get('games').then(res => {
      setData(res.data)
      setGames(res.data.results)
      console.log(res.data.results)
    })
  }

  return (
    <div className='page'>
      <div className={styles.page__filters}>
        Filters
      </div>
      <div className={styles.page__games}>
      {games? (
          <>
           {games.map(game => 
            <div className={styles.game} key={game.id}>
              <div className={styles.game__header}>
                <div className={styles.game__header__left}>
                  <a href={`/games/${game.slug}`} className={styles.title}>{game.title}</a>
                  <span>by</span>
                  <a href={`/users/${game.author.username}`}>{game.author.username}</a>
                </div>                
                <span># scores submitted: {game.scores}</span>
              </div>
              <div className={styles.game__body}>
                <img src={`http://127.0.0.1:8000/${game.thumbnail}`} alt={game.title} />
                <p>{game.description}</p>
              </div>
              {name == game.author.email? (
                <a href={`/games/${game.slug}/edit`} className='btn'>Edit</a>
              ): (null)}
            </div>
           )}
          </>
        ): (<p>Loading...</p>)}
      </div>
    </div>
  )
}

export default Home
