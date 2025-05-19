import estilos from './Fundamentos.module.css'
import Botao from '../../componentes/Botao/Botao'
import Contador from '../../componentes/Contador/Contador'

export default function Fundamentos(){

    const mensagem = (texto) => alert(`Mensagem: ${texto}`)

    return(
        <div className={estilos.conteiner}>

            <p className={estilos.titulo}>Fundamentos</p>

            <p className={estilos.subtitulo}>Props</p>

            <div className={estilos.conteinerBotoes}>
                <Botao 
                    titulo='Entrar' 
                    acao={() => mensagem('Entrar')} 
                />
                <Botao 
                    titulo='Cancelar' 
                    acao={() => mensagem('Cancelar')}
                />
                <Botao 
                    titulo='Ok' 
                    acao={() => mensagem('ok')}
                />
                <Botao 
                    titulo='Encaminhar' 
                    acao={() => mensagem('Encaminhar')}
                />
            </div>

            <p className={estilos.subtitulo}>State</p>
            <Contador />

        </div>
    )
}

