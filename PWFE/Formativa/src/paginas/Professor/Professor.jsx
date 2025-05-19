import estilos from './Professor.module.css'
import {useForm} from 'react-hook-form'
import {z} from 'zod'
import {zodResolver} from '@hookform/resolvers/zod'

const professorSchema = z.object({  

    ni: z.string().length(7, {message: 'NIF incorreto.'}),
    
    nome: z.string().min(2, {message: 'O nome deve conter no mínimo 2 caracteres.'})
                    .max(80, {message: 'O nome deve conter no máximo 80 caracteres.'}),
    email: z.string().email({message: 'Informe um e-mail válido.'}),
    
    telefone: z.string().regex(/^\(\d{2}\) \d{5}-\d{4}$/, 'O telefone deve estar no formato (XX) XXXXX-XXXX'),
    
    dataNascimento: z.string().refine((nascimento) => { let data_nascimento = new Date(nascimento)
                                                        return data_nascimento <= new Date()
                                                      }, 'A data não pode ser no futuro.'),
    
    dataContratacao: z.string().length(10, {message: 'A data de contratação deve ser informada.'}),
    
    disciplinas: z.string().min(1, {message: 'O campo não deve ficar vazio.'})
})

export default function Professor(){

    const {
        register, 
        handleSubmit, 
        formState: {errors}
    } = useForm({
        resolver: zodResolver(professorSchema)
    })

    function autenticarProfessor(data){
        console.log(data)
    }

    return(
        <div className={estilos.conteiner}>
            <p className={estilos.titulo}>Professor</p>

            <form 
                onSubmit={handleSubmit(autenticarProfessor)}
                className={estilos.formulario}
            >
                <input 
                    {...register('ni')}
                    placeholder='NI'
                    className={estilos.campo}
                />
                { errors.ni && (
                    <p className={estilos.mensagem}>
                        {errors.ni.message}
                    </p>
                )}

                <input 
                    {...register('nome')}
                    placeholder='Nome'
                    className={estilos.campo}
                />
                { errors.nome && (
                    <p className={estilos.mensagem}>
                        {errors.nome.message}
                    </p>
                )}

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
                    {...register('telefone')}
                    placeholder='Telefone'
                    className={estilos.campo}
                />
                { errors.telefone && (
                    <p className={estilos.mensagem}>
                        {errors.telefone.message}
                    </p>
                )}


                <input 
                    {...register('dataNascimento')}
                    className={estilos.campo}
                    type='date'
                />
                { errors.dataNascimento && (
                    <p className={estilos.mensagem}>
                        {errors.dataNascimento.message}
                    </p>
                )}


                <input 
                    {...register('dataContratacao')}
                    className={estilos.campo}
                    type='date'
                />
                { errors.dataContratacao && (
                    <p className={estilos.mensagem}>
                        {errors.dataContratacao.message}
                    </p>
                )}


                <input 
                    {...register('disciplinas')}
                    className={estilos.campo}
                    placeholder='Disciplinas'
                />
                { errors.disciplinas && (
                    <p className={estilos.mensagem}>
                        {errors.disciplinas.message}
                    </p>
                )}

                <button
                    className={estilos.botao}
                >Confirmar</button>
            </form>
        </div>
    )
}