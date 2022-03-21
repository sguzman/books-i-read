(import py_data
  [exec :as data]
)

(defn exec [data]
  (list
    (filter
      (fn
        [row]
        (= (get row 18) "read")
      )
      data
    )
  )
)

(defn main []
  (for [row (data)]
    (print row)
  )
)

(if (= __name__ "__main__")
  (main)
)
(defn exec [filename]
  filename)

(defn main []
  (print (exec (arg))))

(if (= __name__ "main")
  (main))
