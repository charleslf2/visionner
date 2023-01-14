import React from 'react'
import Header from '../src/lib/Header'
import styles from "../src/App.module.css"
import Description from './lib/Description'


const App = () => {
  return (
    <div className={styles.wrapper}>

      <div className={styles.container}>

        <Header/>
        <Description/>

      </div>

    </div>
  )
}

export default App