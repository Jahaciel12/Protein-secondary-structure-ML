import requests

url = "https://search.rcsb.org/rcsbsearch/v2/query"

#parametros de busqueda pdb
query = {
  "query": {
    "type": "group",
    "logical_operator": "and",
    "nodes": [
      {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "exptl.method",
          "operator": "exact_match",
          "negation": False,
          "value": "X-RAY DIFFRACTION"
        }
      },
      {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "rcsb_entry_info.diffrn_resolution_high.value",
          "operator": "less_or_equal",
          "negation": False,
          "value": 3
        }
      },
      {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "rcsb_entry_info.deposited_polymer_entity_instance_count",
          "operator": "less_or_equal",
          "negation": False,
          "value": 2
        }
      },
      {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "rcsb_entry_info.deposited_model_count",
          "operator": "equals",
          "negation": False,
          "value": 1
        }
      },
      {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "rcsb_entry_info.selected_polymer_entity_types",
          "operator": "exact_match",
          "negation": False,
          "value": "Protein (only)"
        }
      }
    ],
    "label": "text"
  },
  "return_type": "entry",
  "request_options": {
    "paginate": {
      "start": 0,
      "rows": 10000
    },
    "results_content_type": [
      "experimental"
    ],
    "sort": [
      {
        "sort_by": "score",
        "direction": "desc"
      }
    ],
    "scoring_strategy": "combined"
  }
}

#acceso y respuesta api
#hay un limite de 10000 respuestas

def ask_for_ids(url, json, respuestas = 10000):
  start = 0
  pdb_ides_total = []

  while True:

    json["request_options"]["paginate"]["start"] = start
    json["request_options"]["paginate"]["rows"] = respuestas
    respuesta = requests.post(url, json=json)

    if respuesta.status_code == 200:
        resultado = respuesta.json()
        pdb_ids = [entry["identifier"] for entry in resultado["result_set"]]
        pdb_ides_total.extend(pdb_ids)
        print('si')
        if len(pdb_ids) < respuestas:
          break

        start += respuestas
    else:
        print(f"Error en la consulta: {respuesta.status_code}")
        break

  return pdb_ides_total


ides = ask_for_ids(url, query)
with open('pdb_ides.txt', 'w') as file:
  for id in ides:
    file.write(id + '\n')
