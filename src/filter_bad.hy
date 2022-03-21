(import py_data
  [exec :as data]
)

(defn exec [data]
  (list
    (filter
      (fn [row] (= (len row) 31))
      data
    ))
)

(defn main []
  (exec (data))
)

(if (= __name__ "__main__")
  (main)
)