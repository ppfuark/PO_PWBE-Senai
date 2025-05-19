import estilos from './Reserva.module.css'
import {useForm} from 'react-hook-form'
import {z} from 'zod'
import {zodResolver} from '@hookform/resolvers/zod'

const reservaSchema = z.object({  
  dataInicio: z.string().length(10, {message: 'A data de início deve ser informada.'}),
  dataTermino: z.string().length(10, {message: 'A data de término deve ser informada.'}),
  periodo: z.string().min(1, {message: 'O campo não deve ficar vazio.'}),
  sala: z.string().min(1, {message: 'A sala deve ser informada.'}),
  professor: z.string().min(1, {message: 'O professor deve ser informado.'}),
  disciplina: z.string().min(1, {message: 'A disciplina deve ser informada.'}),
})

export default function Reserva(){
  const {
    register, 
    handleSubmit, 
    formState: {errors}
  } = useForm({
    resolver: zodResolver(reservaSchema)
  })

  function autenticarReserva(data){
    console.log(data)
  }

  return(
    <div className={estilos.container}>
      <p className={estilos.titulo}>Reserva</p>
      <form 
        onSubmit={handleSubmit(autenticarReserva)}
        className={estilos.formulario}
      >
        <input {...register('dataInicio')} className={estilos.campo} type='date' />
        { errors.dataInicio && <p className={estilos.mensagem}>{errors.dataInicio.message}</p> }
        
        <input {...register('dataTermino')} className={estilos.campo} type='date' />
        { errors.dataTermino && <p className={estilos.mensagem}>{errors.dataTermino.message}</p> }
        
        <input {...register('periodo')} placeholder='Período' className={estilos.campo} />
        { errors.periodo && <p className={estilos.mensagem}>{errors.periodo.message}</p> }
        
        <input {...register('sala')} placeholder='Sala' className={estilos.campo} />
        { errors.sala && <p className={estilos.mensagem}>{errors.sala.message}</p> }
        
        <input {...register('professor')} placeholder='Professor' className={estilos.campo} />
        { errors.professor && <p className={estilos.mensagem}>{errors.professor.message}</p> }
        
        <input {...register('disciplina')} placeholder='Disciplina' className={estilos.campo} />
        { errors.disciplina && <p className={estilos.mensagem}>{errors.disciplina.message}</p> }
        
        <button className={estilos.botao}>Reservar</button>
      </form>
    </div>
  )
}
