class Matrix:
    def __init__(self, data):
        self._validate_matrix_rows(data)
        self.data = (data)

    def __str__(self):

    def get_lenghts_padding(self):
        self = [0*]
        for row in self.data:
            for value in row:


    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError("Matrices must have same shape")

        result_data = []
        for row_self, row_other in zip(self.data, other.data):
            row = []
            for value_self, value_other in zip(row_self, row_other):
                row.append(value_self + value_other)
            result_data.append(row)
        return Matrix(result_data)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError("Matrices must have same shape")

        result_data = []
        for row_self, row_other in zip(self.data, other.data):
            row = []
            for value_self, value_other in zip(row_self, row_other):
                row.append(value_self - value_other)
            result_data.append(row) 
        return Matrix(result_data)

    def _validate_matrix_rows(self, data):
        if not data or not data[0]:
            raise ValueError("Matrix must contain at least one non-empty row")
        
        expected_row_length = len(data[0])

        for row_number, row in enumerate(data, start=1):
            if len(row) != expected_row_length:
                raise ValueError(
                    f"Row {row_number} has length {len(row)}, "
                    f"expected {expected_row_length}"
                )
    @property
    def shape(self):
        return (len(self.data), len(self.data[0]))

matr = Matrix([[2,3], [9,3], [4,0]])
matr2 = Matrix([[4,2], [4,2], [2, 5]])
print((matr - matr2).data)



