import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./Components/home/home.component";
import {LoginComponent} from "./Components/login/login.component";
import {ContactoComponent} from "./Components/contacto/contacto.component";
import {SobreMiComponent} from "./Components/sobre-mi/sobre-mi.component";
import {ExperienciaComponent} from "./Components/experiencia/experiencia.component";

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path:'login', component:LoginComponent},
  { path:'contacto', component:ContactoComponent},
  { path:'sobreMi', component:SobreMiComponent},
  { path:'experiencia', component: ExperienciaComponent}
];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
