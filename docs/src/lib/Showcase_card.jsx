import React from 'react'
import styles from "../styles/Showcase_card.module.css"

const Showcase_card = (props) => {
  return (
    <div className={styles.container}>
        <div className={styles.card}>
            <p className={styles.title}>{props.title}</p>
            <img src={props.src} className={styles.image}/>
        </div>
    </div>
  )
}

export default Showcase_card