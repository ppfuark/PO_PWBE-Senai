import estilos from './Sala.module.css'
import {useForm} from 'react-hook-form'
import {z} from 'zod'
import {zodResolver} from '@hookform/resolvers/zod'

const salaSchema = z.object({  

    descricao: z.string().min(2, {message: 'A descrição deve conter no mínimo 2 caracteres.'})
                         .max(80, {message: 'A descrição deve conter no máximo 80 caracteres.'}),
    localizacao: z.string().min(2, {message: 'A localização deve conter no mínimo 2 caracteres.'})
                           .max(40, {message: 'A localização deve conter no máximo 80 caracteres.'})
})

export default function Sala(){

    const {
        register, 
        handleSubmit, 
        formState: {errors}
    } = useForm({
        resolver: zodResolver(salaSchema)
    })

    function autenticarSala(data){
        console.log(data)
    }

    return(
        <div className={estilos.conteiner}>
            <p className={estilos.titulo}>Sala</p>

            <form 
                onSubmit={handleSubmit(autenticarSala)}
                className={estilos.formulario}
            >
                <input 
                    {...register('descricao')}
                    placeholder='Descrição'
                    className={estilos.campo}
                />
                { errors.descricao && (
                    <p className={estilos.mensagem}>
                        {errors.descricao.message}
                    </p>
                )}

                <input 
                    {...register('localizacao')}
                    placeholder='Localização'
                    className={estilos.campo}
                />
                { errors.localizacao && (
                    <p className={estilos.mensagem}>
                        {errors.localizacao.message}
                    </p>
                )}

                <button
                    className={estilos.botao}
                >Confirmar</button>
            </form>
        </div>
    )
}