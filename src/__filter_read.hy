(defn exec [list]
  (list
    (filter
      (fn [row] (= (get row 18) "read"))
      list)))