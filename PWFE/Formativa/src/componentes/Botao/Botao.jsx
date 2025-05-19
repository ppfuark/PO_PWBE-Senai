import estilos from './Botao.module.css'

export default function Botao({ titulo, acao }) {
  return (
    <div 
      className={estilos.conteiner}
      onClick={acao}
    >
      <p className={estilos.texto}>{titulo}</p>
    </div>
  )
}
