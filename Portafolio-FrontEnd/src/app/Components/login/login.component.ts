import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  usuario: FormGroup;
  usernameIncomp:boolean = false;
  passwordIncomp:boolean = false;
  respuesta:string = '';
  resp:boolean = false;
  incomp:boolean = true;

  constructor(private http: HttpClient, private fb:FormBuilder) {
    this.usuario = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    })
  }

  ngOnInit(): void {

  }

  login() {
    if (this.usuario.valid) {
      this.incomp = true;
      this.http.post('http://127.0.0.1:8000/login/', this.usuario.value).subscribe(
        (response) => {
          console.log('Sesión iniciada', response);
          this.respuesta = '¡Ingreso exitoso!';
          this.resp = false;
        },
        (error) => {
          console.error('Error al enviar el correo electrónico', this.usuario.value);
          this.respuesta = 'No se pudo enviar el correo electrónico, intente más tarde';
          this.resp = false;
        }
      );
    }
    else{
      this.usernameIncomp= this.usuario.value.username == '';
      this.passwordIncomp= this.usuario.value.password == '';
      this.resp = true;
      this.incomp = false;
    }
  }

}
