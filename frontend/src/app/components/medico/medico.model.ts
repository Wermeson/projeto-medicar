import { Especialidade } from "./../especialidades/especialidade.model";
export interface Medico {
  id?: number;
  nome: string;
  crm: string;
  email: string;
  telefone: string;
  especialidade_id: number;
}
