import React from 'react'
import styles from "../styles/Descr.module.css"


const Description = () => {
  return (
    <div className={styles.container}>

        <h2 className={styles.title}>About Visionner ?</h2>

        <p className={styles.content}>
          <p>Visionner (<span>from the french , that refer to technical looking</span>)</p>
          <p>Is a python package that help you start your next computer vision project with confidence.</p>
        
        </p>

    </div>
  )
}

export default Description