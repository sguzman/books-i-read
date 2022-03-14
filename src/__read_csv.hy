(import csv)

(defn exec [filename]
  (list ((. csv read) filename)))