import React from 'react'
import styles from "../styles/Showcase_card.module.css"

const Showcase_card = (props) => {
  return (
    <div className={styles.container}>
        <div className={styles.title}>
            <p>{props.title}</p>
            <img src={props.src}/>
        </div>
    </div>
  )
}

export default Showcase_card