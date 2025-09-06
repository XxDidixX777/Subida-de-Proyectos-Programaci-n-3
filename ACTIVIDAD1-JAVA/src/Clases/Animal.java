/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;

import java.time.LocalDate;

/**
 *
 * @author Didier
 */
public class Animal {
     private String nombre;
    private double peso;
    private String propietario;
    private LocalDate fechaCumpleaños;
    private LocalDate fechaUltimaVacuna;
    
     public Animal(String nombre, double peso, String propietario, LocalDate fechaCumpleaños, LocalDate fechaUltimaVacuna) {
        this.nombre = nombre;
        this.peso = peso;
        this.propietario = propietario;
        this.fechaCumpleaños = fechaCumpleaños;
        this.fechaUltimaVacuna = fechaUltimaVacuna;
    }

    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /**
     * @return the peso
     */
    public double getPeso() {
        return peso;
    }

    /**
     * @param peso the peso to set
     */
    public void setPeso(double peso) {
        this.peso = peso;
    }

    /**
     * @return the propietario
     */
    public String getPropietario() {
        return propietario;
    }

    /**
     * @param propietario the propietario to set
     */
    public void setPropietario(String propietario) {
        this.propietario = propietario;
    }

    /**
     * @return the fechaCumpleaños
     */
    public LocalDate getFechaCumpleaños() {
        return fechaCumpleaños;
    }

    /**
     * @param fechaCumpleaños the fechaCumpleaños to set
     */
    public void setFechaCumpleaños(LocalDate fechaCumpleaños) {
        this.fechaCumpleaños = fechaCumpleaños;
    }

    /**
     * @return the fechaUltimaVacuna
     */
    public LocalDate getFechaUltimaVacuna() {
        return fechaUltimaVacuna;
    }

    /**
     * @param fechaUltimaVacuna the fechaUltimaVacuna to set
     */
    public void setFechaUltimaVacuna(LocalDate fechaUltimaVacuna) {
        this.fechaUltimaVacuna = fechaUltimaVacuna;
    }
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Peso: " + peso + " kg");
        System.out.println("Propietario: " + propietario);
        System.out.println("Fecha cumpleaños: " + fechaCumpleaños);
        System.out.println("Ultima vacuna: " + fechaUltimaVacuna);
    }
    
}
