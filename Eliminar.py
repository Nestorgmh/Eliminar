def eliminar_duplicados(arr):
  """
  Elimina los elementos duplicados de un arreglo ordenado de forma ascendente.

  Args:
    arr: Un arreglo de números ordenados de forma ascendente.

  Returns:
    Una tupla (nuevo_arreglo, K), donde:
      - nuevo_arreglo: El arreglo modificado sin duplicados.
      - K: El número de elementos únicos en el arreglo.
  """

  lento = 0
  rapido = 1

  while rapido < len(arr):
    if arr[lento] != arr[rapido]:
      lento += 1
      arr[lento] = arr[rapido]
    rapido += 1

  K = lento + 1
  return arr[:K], K

# Ejemplo de uso:
arreglo = [2, 5, 5, 7, 7, 7, 8, 9]
nuevo_arreglo, K = eliminar_duplicados(arreglo)
print(nuevo_arreglo)  # Imprime: [2, 5, 7, 8, 9]
print(K)  # Imprime: 5