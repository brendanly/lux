from lux.view.ViewCollection import ViewCollection
class ExecutionEngine:
    def __init__(self):
        self.name = "ExecutionEngine"

    def __repr__(self):
        return f"<ExecutionEngine>"
    @staticmethod
    def execute(ldf):
        '''
        Given a ViewCollection, fetch the data required to render the view
        1) Apply filters
        2) Retreive relevant attribute
        3) return a DataFrame with relevant results
        '''
        viewCollection = ldf.viewCollection
        for view in viewCollection:
            filters = view.getFiltersFromSpec()
            if filters:
                ExecutionEngine.executeFilter(view, filters, ldf)

            attributes = []
            xAttribute = view.getObjFromChannel("x")
            yAttribute = view.getObjFromChannel("y")
            zAttribute = view.getObjFromChannel("z")

            if xAttribute and xAttribute[0].attribute:
                attributes.append(xAttribute[0].attribute)
            if yAttribute and yAttribute[0].attribute:
                attributes.append(yAttribute[0].attribute)
            if zAttribute and zAttribute[0].attribute:
                attributes.appeend(zAttribute[0].attribute)

            print(attributes)
            view.data = ldf[attributes]

        # TODO:Select relevant data based on attribute information

        return ldf 

    @staticmethod
    def executeFilter(view, filters, ldf):
        for filter in filters:
            if view.data:
                view.data = view.data[filter.attribute == filter.value]
            else:
                view.data = ldf[filter.attribute == filter.value]