import estilos from './Disciplina.module.css'
import {useForm} from 'react-hook-form'
import {z} from 'zod'
import {zodResolver} from '@hookform/resolvers/zod'

const disciplinaSchema = z.object({  

    nome: z.string().min(2, {message: 'O nome deve conter no mínimo 2 caracteres.'})
                    .max(80, {message: 'O nome deve conter no máximo 80 caracteres.'}),
    curso: z.string().min(2, {message: 'O nome deve conter no mínimo 2 caracteres.'})
                     .max(100, {message: 'O nome deve conter no máximo 100 caracteres.'}),
    cargaHoraria: z.number().min(1, {message: 'Carga horária mínima de 1h.'}),
    descricao: z.string().min(1, {message: 'O campo não deve ficar vazio.'}),                
    responsavel: z.string().min(1, {message: 'O campo não deve ficar vazio.'})
})

export default function Disciplina(){

    const {
        register, 
        handleSubmit, 
        setValue,
        formState: {errors}
    } = useForm({
        resolver: zodResolver(disciplinaSchema)
    })

    function autenticarDisciplina(data){
        console.log(data.email)
        console.log(data.senha)
    }

    // conversão para número
    const conversaoNumero = (e) => {
        let valor = e.target.value
        let valorNumerico = valor ? Number(valor) : undefined
        setValue('cargaHoraria', valorNumerico)
    }

    return(
        <div className={estilos.conteiner}>
            <p className={estilos.titulo}>Disciplina</p>

            <form 
                onSubmit={handleSubmit(autenticarDisciplina)}
                className={estilos.formulario}
            >

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
                    {...register('curso')}
                    placeholder='Curso'
                    className={estilos.campo}
                />
                { errors.curso && (
                    <p className={estilos.mensagem}>
                        {errors.curso.message}
                    </p>
                )}


                <input 
                    {...register('cargaHoraria')}
                    placeholder='Carga horária'
                    className={estilos.campo}
                    type='number'
                    onChange={conversaoNumero}
                    
                />
                { errors.cargaHoraria && (
                    <p className={estilos.mensagem}>
                        {errors.cargaHoraria.message}
                    </p>
                )}


                <input 
                    {...register('descricao')}
                    className={estilos.campo}
                    placeholder='Descrição'
                />
                { errors.descricao && (
                    <p className={estilos.mensagem}>
                        {errors.descricao.message}
                    </p>
                )}


                <input 
                    {...register('responsavel')}
                    className={estilos.campo}
                    placeholder='Responsável'
                />
                { errors.responsavel && (
                    <p className={estilos.mensagem}>
                        {errors.responsavel.message}
                    </p>
                )}

                <button
                    className={estilos.botao}
                >Confirmar</button>
            </form>
        </div>
    )
}