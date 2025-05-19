import estilos from './Login.module.css'
import {useForm} from 'react-hook-form'
import {z} from 'zod'
import {zodResolver} from '@hookform/resolvers/zod'

const loginSchema = z.object({  
    email: z.string()
            .email({message: 'Informe um e-mail válido!'}) ,
    senha: z.string()
            .length(6, {message: 'Defina uma senha de 6 caracteres!'})
})

export default function Login(){

    const {
        register, 
        handleSubmit, 
        formState: {errors}
    } = useForm({
        resolver: zodResolver(loginSchema)
    })

    function autenticarUsuario(data){
        console.log(data.email)
        console.log(data.senha)
    }

    return(
        <div className={estilos.conteiner}>
            <p className={estilos.titulo}>Login</p>

            <form 
                onSubmit={handleSubmit(autenticarUsuario)}
                className={estilos.formulario}
            >
                <input 
                    {...register('email')}
                    placeholder='E-mail'
                    className={estilos.campo}
                />
                { errors.email && (
                    <p className={estilos.mensagem}>
                        {errors.email.message}
                    </p>
                )}

                <input 
                    {...register('senha')}
                    placeholder='Senha'
                    className={estilos.campo}
                />
                { errors.senha && (
                    <p className={estilos.mensagem}>
                        {errors.senha.message}
                    </p>
                )}

                <button
                    className={estilos.botao}
                >Entrar</button>
            </form>
        </div>
    )
}