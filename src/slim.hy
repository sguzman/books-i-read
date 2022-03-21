(import py_data
  [exec :as csv]
)

(defn exec [data]
  (list
    (map
      (fn [x] [
           (get x 1)
           (get x 2)
           (get x 11)
           (get x 14)
        ]
      )
      data
    )
  )
)

(defn main []
  (for [row (exec (csv))]
    (print row)
  )
)

(if (= __name__ "__main__")
  (main)
)