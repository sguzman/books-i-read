(import __read_csv
  [exec :as read]
)

(import __single_arg
  [exec :as arg]
)

(defn exec []
  "Convert csv file into py-friendly array"
  (list (read (arg)))
)

(defn main []
  (for [row (exec)]
    (print row)
  )
)

(if (= __name__ "__main__")
  (main)
)