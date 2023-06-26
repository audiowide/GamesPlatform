import React, { useEffect, useState } from 'react'
import styles from './ManageGame.module.css'
import { useNavigate, useParams } from 'react-router-dom'
import { $axios } from '../../api'
import {useAuth} from '../../hooks/useAuth'

const ManageGame = () => {
  const {slug} = useParams()
  const {navigate} = useNavigate()
  const {name, isAuth} = useAuth()

  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [thumbnail, setThumbnail] = useState('')
  const [file, setFile] = useState('')


  useEffect(() => {
    document.title = `${slug} | Manage Game`
    getData()
  }, [])

  const getData = async () => {
    $axios.get(`games/${slug}`)
      .then(res => {
        console.log(res.data)
        setTitle(res.data.title)
        setThumbnail(res.data.thumbnail)
        setDescription(res.data.description)
      })
  }

  const updateTitle = () => {
    $axios.put(`games/${slug}`, {
      'title': title,
    })
    .then(res => {
      console.log(res.data)
    })
  }

  const updateDescription = () => {
    $axios.put(`games/${slug}`, {
      'description': description,
    })
    .then(res => {
      console.log(res.data)
    })
  }

  const deletegame = () => {
    $axios.delete(`games/${slug}`).then(() => {
      navigate('/')
    })
  }
  
  const uploadFiles = (e) => {
    setFile(e.target.files[0])
    console.log(e)
  }

  return (
    <div className='page'>
        <h2>Manage Game</h2>
        <form className={styles.form}>
          <div className="buttons">
          <input 
            type="text"
            value={title}
            placeholder='Title'
            onChange={e => setTitle(e.target.value)} 
          />
          <a className='btn' onClick={updateTitle}>edit</a>
          </div>
          <div className="buttons">
            <img src={`http://127.0.0.1:8000/${thumbnail}`} className={styles.thumbnail} alt={title} />
            <div className='buttons'>
              <textarea 
                value={description}
                onChange={e => setDescription(e.target.value)}></textarea>
              <a className='btn' onClick={updateDescription}>edit</a>
            </div>
          </div>
          <div className="buttons">
            <input 
              type="file"
              className={styles.file} 
              value={file} 
              onChange={e => uploadFiles(e)}
              />
            <a className='btn' onClick={deletegame}>delete</a>
          </div>
        </form>
    </div>
  )
}

export default ManageGame
