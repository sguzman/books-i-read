(import py_data
 [exec :as data]
)

(defn exec [data]
 "Sort by time read"
 (sorted data
         :key (fn [row] (get row -1))
         :reverse True
 )
)

(defn main []
  (for [row (data)])
  (print row)
  )

(if (= __name__ "__main__")
 (main)
)