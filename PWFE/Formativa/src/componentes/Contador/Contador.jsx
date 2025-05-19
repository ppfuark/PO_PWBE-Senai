import estilos from './Contador.module.css'
import {useState} from 'react'

export default function Contador(){

    const [valor, setValor] = useState(0)

    const somar = () => {
        setValor(valor + 1)
    }

    const subtrair = () => {
        setValor(valor - 1)
    }

    return(
        <div className={estilos.conteiner}>

            <p className={estilos.titulo}>Contador</p>

            <div className={estilos.conteinerBotoes}>

                <div 
                    className={estilos.botao} 
                    onClick={subtrair}
                >-</div>

                <p className={estilos.valor}>{valor}</p>

                <div 
                    className={estilos.botao}
                    onClick={somar}
                >+</div>
            </div>

        </div>
    )
}
