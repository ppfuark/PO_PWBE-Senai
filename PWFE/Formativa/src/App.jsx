import { Routes, Route } from "react-router-dom";

import Inicial from "./paginas/Inicial/Inicial";
import Login from "./paginas/Login/Login";
import Disciplina from "./paginas/Disciplina/Disciplina";
import Fundamentos from "./paginas/Fundamentos/Fundamentos";
import Professor from "./paginas/Professor/Professor";
import Reserva from "./paginas/Reserva/Reserva";
import Sala from "./paginas/Sala/Sala";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Inicial />} />
      <Route path="/login" element={<Login />} />
      <Route path="/disciplina" element={<Disciplina />} />
      <Route path="/ambiente" element={<Sala />} />
      <Route path="/professor" element={<Professor />} />
      <Route path="/reserva" element={<Reserva />} />
    </Routes>
  );
}

export default App;
