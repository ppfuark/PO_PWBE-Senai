import estilos from './Inicial.module.css'
import Cabecalho from '../../componentes/Cabecalho/Cabecalho'
import Lateral from '../../componentes/Lateral/Lateral'
import Principal from '../../componentes/Principal/Principal'
import Rodape from '../../componentes/Rodape/Rodape'

export default function Inicial(){
    return(
        <div className={estilos.gridConteiner}>            
            <Cabecalho />
            <Lateral />
            <Principal />
            <Rodape />
        </div>
    )
}